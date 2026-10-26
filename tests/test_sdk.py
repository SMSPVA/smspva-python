import asyncio
import json
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

import httpx
from smspva import (SMSPVA, AsyncSMSPVA, ApiError, ProtocolError, TransportError,
                    RequestTimeoutError, PollingTimeoutError, ValidationError, is_pending, is_no_stock)

CASES = json.loads((Path(__file__).resolve().parent / "cases.json").read_text(encoding="utf-8"))
SECRET = "sdk-local-key-+&?=/"


class Harness:
    def __init__(self):
        self.received = []
        self.status = 200
        self.body = {"status": 1, "data": []}
        self.failure = None

    def handle(self, request):
        self.received.append(request)
        if self.failure:
            raise self.failure
        if isinstance(self.body, str):
            return httpx.Response(self.status, text=self.body, headers={"Set-Cookie": "session=should-not-return"})
        return httpx.Response(self.status, json=self.body, headers={"Set-Cookie": "session=should-not-return"})

    def client(self, asynchronous=False, key=SECRET):
        cls = AsyncSMSPVA if asynchronous else SMSPVA
        return cls(key, transport=httpx.MockTransport(self.handle))


def assert_wire(case, request):
    url = urlsplit(str(request.url))
    query = parse_qs(url.query)
    assert request.method == case["method"], case["key"]
    path = case["path"]
    for name, value in case["params"].items():
        path = path.replace("{" + name + "}", str(value))
    assert unquote(url.path) == path, case["key"]
    assert query.get("method") == ([case["action"]] if case.get("action") else None), case["key"]
    assert request.headers.get("apikey") == (SECRET if case["family"] == "activation" else None), case["key"]
    assert query.get("apikey") == ([SECRET] if case["family"] != "activation" and case["auth"] != "none" else None), case["key"]
    assert "cookie" not in request.headers
    for name, value in case["params"].items():
        if "{" + name + "}" in case["path"]:
            continue
        if name == "partnerkey":
            assert request.headers.get(name) == str(value)
        else:
            assert query.get(name) == [str(value)], (case["key"], name)


class SyncTests(unittest.TestCase):
    def test_all_56_methods_preserve_wire_contract_and_values(self):
        self.assertEqual(len(CASES), 56)
        h = Harness()
        with h.client() as client:
            for case in CASES:
                with self.subTest(case=case["key"]):
                    h.body = case["response"]
                    h.received.clear()
                    result = getattr(getattr(client, case["family"]), case["pyName"])(**case["params"])
                    self.assertEqual(result, case["response"])
                    self.assertEqual(len(h.received), 1)
                    assert_wire(case, h.received[0])
            self.assertFalse(hasattr(client, "alternative"))
            self.assertNotIn(SECRET, repr(client))

    def test_auth_optional_provider_omission_and_encoding(self):
        h = Harness()
        with h.client() as client:
            for provider in [None, ""]:
                client.email.get_data(pcode=provider)
                self.assertNotIn("pcode=", str(h.received[-1].url))
            client.email.get_data(pcode="provider.new")
            self.assertEqual(h.received[-1].url.params["pcode"], "provider.new")
            client.rental.get_data(country="UK", use_api_key=False)
            self.assertNotIn("apikey", h.received[-1].url.params)
            client.email.get_mails(orderid=123, sq="code: +a & 中文 /?")
            self.assertEqual(h.received[-1].url.params["sq"], "code: +a & 中文 /?")
            h.body = {"statusCode": 200, "data": []}
            client.activation.get_operators(country="UK /+&?中文")
            self.assertEqual(unquote(urlsplit(str(h.received[-1].url)).path), "/activation/operators/UK /+&?中文")
        h.body = {"status": 1, "data": []}
        with h.client(key=None) as client:
            client.email.get_providers()
            client.rental.get_countries()
            self.assertNotIn("apikey", str(h.received[-1].url))

    def test_pending_and_no_stock_are_results_not_generic_errors(self):
        h = Harness()
        with h.client() as client:
            h.status, h.body = 202, {"statusCode": 202, "error": {"type": "SMS_NOT_YET_RECEIVED"}}
            self.assertTrue(is_pending(client.activation.receive_sms(orderid=123)))
            h.status, h.body = 200, {"status": 2}
            self.assertTrue(is_no_stock(client.email.create_order(scode="twitter", dtype="week", dcount=1)))
            with self.assertRaises(ApiError):
                client.email.get_orders()

    def test_errors_preserve_status_and_payload_without_url_in_exception(self):
        h = Harness()
        with h.client() as client:
            for body in [{"status": 0, "msg": "Incorrect order id"}, {"status": 0, "errorid": 9, "errormsg": "Provider not found"}]:
                h.body = body
                with self.assertRaises(ApiError) as error:
                    client.email.get_orders()
                self.assertEqual(error.exception.response, body)
                self.assertEqual(error.exception.http_status, 200)
                self.assertNotIn(SECRET, str(error.exception))
            h.status, h.body = 410, {"statusCode": 410, "error": {"type": "ORDER_CLOSED"}}
            with self.assertRaises(ApiError) as error:
                client.activation.receive_sms(orderid=123)
            self.assertEqual(error.exception.code, "ORDER_CLOSED")
            self.assertEqual(error.exception.http_status, 410)
            h.status, h.body = 503, {"status": 1}
            with self.assertRaises(ApiError):
                client.rental.get_countries()
            h.status = 200
            for body in ["", "<html>Unavailable</html>", "null", "[]", {}, {"status": "1"}, {"status": True}]:
                h.body = body
                with self.assertRaises(ProtocolError):
                    client.rental.get_countries()

    def test_validation_makes_no_request(self):
        h = Harness()
        with h.client() as client:
            for call in [
                lambda: client.activation.receive_sms(orderid=True),
                lambda: client.activation.get_number(country="UK", service="opt20", voice=3),
                lambda: client.activation.get_operators(country=".."),
                lambda: client.email.create_order(scode="twitter", dtype="week", dcount=0),
                lambda: client.email.get_orders(timeout=float("nan")),
            ]:
                with self.assertRaises(ValidationError):
                    call()
            with self.assertRaises(TypeError):
                client.rental.get_multi_service_count(country="UK", services="opt20,opt29")
            self.assertEqual(len(h.received), 0)
        with self.assertRaises(ValidationError):
            SMSPVA("key\r\nHeader: injected")
        with self.assertRaises(ValidationError):
            SMSPVA(email_base_url="https://key:secret@example.com")
        with h.client(key=None) as client, self.assertRaises(ValidationError):
            client.activation.get_balance()

    def test_transport_failures_never_retry(self):
        h = Harness()
        with h.client() as client:
            for failure, cls in [(httpx.ReadTimeout("URL with " + SECRET), RequestTimeoutError), (httpx.ConnectError("URL with " + SECRET), TransportError)]:
                h.received.clear()
                h.failure = failure
                with self.assertRaises(cls) as error:
                    client.email.create_order(scode="twitter", dtype="week", dcount=1)
                self.assertTrue(error.exception.outcome_unknown)
                self.assertNotIn(SECRET, str(error.exception))
                self.assertEqual(len(h.received), 1)

    def test_polling_deadline_and_terminal_state(self):
        h = Harness()
        with h.client() as client:
            h.body = {"statusCode": 200, "data": {"sms": {"code": "12:34"}}}
            self.assertEqual(client.activation.wait_for_sms(orderid=123, expires_at=time.time() + 1)["data"]["sms"]["code"], "12:34")
            h.received.clear()
            with self.assertRaises(PollingTimeoutError):
                client.activation.wait_for_sms(orderid=123, expires_at=time.time() - 1)
            self.assertFalse(h.received)
            h.status, h.body = 202, {"statusCode": 202, "error": {"type": "SMS_NOT_YET_RECEIVED"}}
            with self.assertRaises(PollingTimeoutError):
                client.activation.wait_for_sms(orderid=123, expires_at=time.time() + .05)
            self.assertEqual(len(h.received), 1)
            h.status, h.body = 410, {"statusCode": 410, "error": {"type": "ORDER_CLOSED"}}
            h.received.clear()
            with self.assertRaises(ApiError):
                client.activation.wait_for_sms(orderid=123, expires_at=time.time() + 1)
            self.assertEqual(len(h.received), 1)


class AsyncTests(unittest.IsolatedAsyncioTestCase):
    async def test_all_56_methods_async(self):
        h = Harness()
        async with h.client(asynchronous=True) as client:
            for case in CASES:
                with self.subTest(case=case["key"]):
                    h.body = case["response"]
                    h.received.clear()
                    result = await getattr(getattr(client, case["family"]), case["pyName"])(**case["params"])
                    self.assertEqual(result, case["response"])
                    self.assertEqual(len(h.received), 1)
                    assert_wire(case, h.received[0])

    async def test_async_errors_pending_no_stock_and_close(self):
        h = Harness()
        async with h.client(asynchronous=True) as client:
            h.status, h.body = 202, {"statusCode": 202, "error": {"type": "SMS_NOT_YET_RECEIVED"}}
            self.assertTrue(is_pending(await client.activation.receive_sms(orderid=123)))
            with self.assertRaises(PollingTimeoutError):
                await client.activation.wait_for_sms(orderid=123, expires_at=time.time() + .05)
            h.status, h.body = 200, {"status": 2}
            self.assertTrue(is_no_stock(await client.email.create_order(scode="twitter", dtype="week", dcount=1)))
            h.body = {"status": 0, "errorid": 9, "errormsg": "Provider not found"}
            with self.assertRaises(ApiError) as error:
                await client.email.get_orders()
            self.assertEqual(error.exception.code, 9)
            h.body = "not json"
            with self.assertRaises(ProtocolError):
                await client.email.get_orders()
        self.assertTrue(client._transport._client.is_closed)

    async def test_async_cancellation_and_timeout_no_retries(self):
        calls = []
        async def handle(request):
            calls.append(request)
            await asyncio.sleep(10)
            return httpx.Response(200, json={"status": 1})
        async with AsyncSMSPVA(SECRET, transport=httpx.MockTransport(handle)) as client:
            task = asyncio.create_task(client.email.create_order(scode="twitter", dtype="week", dcount=1))
            await asyncio.sleep(.02)
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task
            self.assertEqual(len(calls), 1)
        h = Harness()
        h.failure = httpx.ReadTimeout("secret " + SECRET)
        async with h.client(asynchronous=True) as client:
            with self.assertRaises(RequestTimeoutError) as error:
                await client.email.create_order(scode="twitter", dtype="week", dcount=1)
            self.assertTrue(error.exception.outcome_unknown)
            self.assertNotIn(SECRET, str(error.exception))
            self.assertEqual(len(h.received), 1)


class LoopbackTests(unittest.IsolatedAsyncioTestCase):
    async def test_real_sync_and_async_http_and_redirect_refusal(self):
        requests = []
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass
            def do_GET(self):
                requests.append((self.command, self.path, dict(self.headers)))
                if self.path.startswith("/api/rent.php"):
                    self.send_response(302)
                    self.send_header("Location", "/must-not-follow")
                    body = b'{}'
                else:
                    self.send_response(200)
                    body = b'{"statusCode":200,"data":{"balance":"10.50"}}'
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        base = f"http://127.0.0.1:{server.server_port}"
        try:
            with SMSPVA(SECRET, activation_base_url=base, rental_base_url=base) as client:
                self.assertEqual(client.activation.get_balance()["data"]["balance"], "10.50")
                with self.assertRaises(ApiError):
                    client.rental.get_countries()
            async with AsyncSMSPVA(SECRET, activation_base_url=base) as client:
                self.assertEqual((await client.activation.get_balance())["data"]["balance"], "10.50")
            self.assertEqual(len(requests), 3)
            self.assertEqual(requests[0][2].get("apikey"), SECRET)
        finally:
            server.shutdown()
            server.server_close()
            worker.join()


if __name__ == "__main__":
    unittest.main()
