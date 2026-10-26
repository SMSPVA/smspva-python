from __future__ import annotations

import json
import math
import re
from importlib.resources import files
from typing import Any
from urllib.parse import quote, urlencode, urlsplit

import httpx

from .errors import ApiError, ProtocolError, RequestTimeoutError, TransportError, ValidationError

OPERATIONS: dict[str, Any] = json.loads(files("smspva").joinpath("_contracts.json").read_text(encoding="utf-8"))["operations"]


def positive_timeout(value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        raise ValidationError("timeout must be a finite positive number of seconds")
    return value


def base_url(value: str) -> str:
    try:
        url = urlsplit(value)
        valid = url.scheme in {"http", "https"} and url.hostname and not (url.username or url.password or url.query or url.fragment)
        _ = url.port
    except (TypeError, ValueError):
        valid = False
    if not valid:
        raise ValidationError("Base URL must use HTTP(S) without credentials, query or fragment")
    return value.rstrip("/")


class Configuration:
    def __init__(self, api_key: str | None, timeout: float, bases: dict[str, str | None]):
        if api_key is not None and (not isinstance(api_key, str) or not api_key or "\r" in api_key or "\n" in api_key):
            raise ValidationError("api_key must be a non-empty string without line breaks")
        self._api_key = api_key
        self.timeout = positive_timeout(timeout)
        self._bases = {k: base_url(v) for k, v in bases.items() if v is not None}

    def prepare(self, key: str, params: dict[str, Any], use_api_key: bool) -> tuple[dict[str, Any], str, dict[str, str]]:
        op = OPERATIONS[key]
        allowed = {p["name"] for p in op["params"]}
        if params.keys() - allowed:
            raise ValidationError("Unexpected request parameter")
        query: dict[str, str] = {"method": op["action"]} if op.get("action") else {}
        headers = {"Accept": "application/json"}
        path = op["path"]
        for p in op["params"]:
            name, schema = p["name"], p["schema"]
            value = params.get(name)
            if value is None or (p.get("omitEmpty") and value == ""):
                if p["required"]:
                    raise ValidationError(f"Missing required parameter: {name}")
                continue
            kind = schema.get("type")
            if ((kind == "integer" and (isinstance(value, bool) or not isinstance(value, int)))
                or (kind == "number" and (isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value)))
                or (kind == "string" and not isinstance(value, str)) or (kind == "boolean" and not isinstance(value, bool))):
                raise ValidationError(f"Invalid type for parameter: {name}")
            if ("enum" in schema and value not in schema["enum"]
                or isinstance(value, (int, float)) and ("minimum" in schema and value < schema["minimum"] or "maximum" in schema and value > schema["maximum"])
                or isinstance(value, str) and ("minLength" in schema and len(value) < schema["minLength"] or "maxLength" in schema and len(value) > schema["maxLength"] or "pattern" in schema and not re.search(schema["pattern"], value))):
                raise ValidationError(f"Invalid value for parameter: {name}")
            text = str(value)
            if p["in"] == "path":
                if text in {".", ".."}:
                    raise ValidationError(f"Invalid path parameter: {name}")
                path = path.replace("{" + name + "}", quote(text, safe=""))
            elif p["in"] == "header":
                if "\r" in text or "\n" in text:
                    raise ValidationError(f"Invalid header: {name}")
                headers[name] = text
            else:
                query[name] = text
        if op["auth"] == "required" and not self._api_key:
            raise ValidationError("Set api_key for this operation")
        if self._api_key and op["auth"] != "none" and (op["auth"] == "required" or use_api_key):
            if op["family"] == "activation":
                headers["apikey"] = self._api_key
            else:
                query["apikey"] = self._api_key
        url = self._bases.get(op["family"], op["baseUrl"].rstrip("/")) + path
        if query:
            url += "?" + urlencode(query)
        return op, url, headers


def parse_response(op: dict[str, Any], key: str, response: httpx.Response) -> dict[str, Any]:
    family, http_status = op["family"], response.status_code
    try:
        value = response.json()
    except (ValueError, UnicodeDecodeError):
        raise ProtocolError(family, key, http_status) from None
    if not isinstance(value, dict):
        raise ProtocolError(family, key, http_status)
    raw_error = value.get("error")
    error: dict[str, Any] = raw_error if isinstance(raw_error, dict) else {}
    status = value.get("statusCode" if family == "activation" else "status")
    raw_code = error.get("type", value.get("errorid", status))
    code: str | int = raw_code if isinstance(raw_code, (str, int)) and not isinstance(raw_code, bool) else http_status
    if not 200 <= http_status < 300:
        raise ApiError(family, key, http_status, code, value)
    if isinstance(status, bool) or not isinstance(status, int):
        raise ProtocolError(family, key, http_status)
    if op["pending"] and http_status == 202 and status == 202 and error.get("type") == "SMS_NOT_YET_RECEIVED":
        return value
    if op["noStock"] and http_status == 200 and status == 2:
        return value
    if (status != 200 or value.get("error")) if family == "activation" else status != 1:
        raise ApiError(family, key, http_status, code, value)
    return value


class Transport(Configuration):
    def __init__(self, api_key: str | None, timeout: float, bases: dict[str, str | None], transport: httpx.BaseTransport | None):
        super().__init__(api_key, timeout, bases)
        self._client = httpx.Client(transport=transport, follow_redirects=False, trust_env=False)

    def request(self, key: str, params: dict[str, Any], *, timeout: float | None = None, use_api_key: bool = True) -> dict[str, Any]:
        op, url, headers = self.prepare(key, params, use_api_key)
        limit = positive_timeout(self.timeout if timeout is None else timeout)
        try:
            request = self._client.build_request(op["method"], url, headers=headers, timeout=limit)
            request.headers.pop("cookie", None)
            response = self._client.send(request, follow_redirects=False)
        except httpx.TimeoutException:
            raise RequestTimeoutError(op["family"], key, op["stateful"], "timeout") from None
        except httpx.TransportError:
            raise TransportError(op["family"], key, op["stateful"]) from None
        return parse_response(op, key, response)

    def close(self) -> None:
        self._client.close()


class AsyncTransport(Configuration):
    def __init__(self, api_key: str | None, timeout: float, bases: dict[str, str | None], transport: httpx.AsyncBaseTransport | None):
        super().__init__(api_key, timeout, bases)
        self._client = httpx.AsyncClient(transport=transport, follow_redirects=False, trust_env=False)

    async def request(self, key: str, params: dict[str, Any], *, timeout: float | None = None, use_api_key: bool = True) -> dict[str, Any]:
        op, url, headers = self.prepare(key, params, use_api_key)
        limit = positive_timeout(self.timeout if timeout is None else timeout)
        try:
            request = self._client.build_request(op["method"], url, headers=headers, timeout=limit)
            request.headers.pop("cookie", None)
            response = await self._client.send(request, follow_redirects=False)
        except httpx.TimeoutException:
            raise RequestTimeoutError(op["family"], key, op["stateful"], "timeout") from None
        except httpx.TransportError:
            raise TransportError(op["family"], key, op["stateful"]) from None
        return parse_response(op, key, response)

    async def close(self) -> None:
        await self._client.aclose()
