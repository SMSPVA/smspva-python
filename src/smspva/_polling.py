from __future__ import annotations

import asyncio
import math
import time
from typing import Any
from typing_extensions import TypeIs

from ._transport import Transport, AsyncTransport
from .errors import PollingTimeoutError, RequestTimeoutError, ValidationError
from .types import ActivationPending, EmailCreateOrderResponseVariant1


def is_pending(value: Any) -> TypeIs[ActivationPending]:
    return isinstance(value, dict) and value.get("statusCode") == 202 and isinstance(value.get("error"), dict) and value["error"].get("type") == "SMS_NOT_YET_RECEIVED"


def is_no_stock(value: Any) -> TypeIs[EmailCreateOrderResponseVariant1]:
    return isinstance(value, dict) and value.get("status") == 2


def deadline(expires_at: float, interval: float) -> float:
    if not math.isfinite(expires_at) or not math.isfinite(interval) or interval < 5:
        raise ValidationError("Use a finite epoch expires_at and an interval of at least 5 seconds")
    return time.monotonic() + (expires_at - time.time())


def wait_for_sms(transport: Transport, orderid: int, expires_at: float, interval: float, partnerkey: str | None) -> dict[str, Any]:
    end = deadline(expires_at, interval)
    while time.monotonic() < end:
        remaining = end - time.monotonic()
        result = transport.request("activation.receiveSms", {"orderid": orderid, "partnerkey": partnerkey}, timeout=max(0.001, min(transport.timeout, remaining)))
        if time.monotonic() >= end:
            raise PollingTimeoutError()
        if not is_pending(result):
            return result
        left = end - time.monotonic()
        time.sleep(max(0, min(interval, left)))
        if left <= interval:
            raise PollingTimeoutError()
    raise PollingTimeoutError()


async def async_wait_for_sms(transport: AsyncTransport, orderid: int, expires_at: float, interval: float, partnerkey: str | None) -> dict[str, Any]:
    end = deadline(expires_at, interval)
    while time.monotonic() < end:
        remaining = end - time.monotonic()
        try:
            result = await asyncio.wait_for(transport.request("activation.receiveSms", {"orderid": orderid, "partnerkey": partnerkey}, timeout=max(0.001, min(transport.timeout, remaining))), timeout=remaining)
        except asyncio.TimeoutError:
            raise RequestTimeoutError("activation", "activation.receiveSms", True, "timeout") from None
        if not is_pending(result):
            return result
        left = end - time.monotonic()
        await asyncio.sleep(max(0, min(interval, left)))
        if left <= interval:
            raise PollingTimeoutError()
    raise PollingTimeoutError()
