# SMSPVA Python SDK

[![CI](https://github.com/SMSPVA/smspva-python/actions/workflows/ci.yml/badge.svg)](https://github.com/SMSPVA/smspva-python/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/SMSPVA/smspva-python/blob/main/LICENSE) ![Status: alpha](https://img.shields.io/badge/status-alpha-orange.svg)

Official Python client for [SMSPVA](https://smspva.com/), a service for receiving verification SMS, renting phone numbers and renting private email addresses. Integrate these APIs into Python applications with synchronous **SMSPVA** and asynchronous **AsyncSMSPVA** clients.

Requires Python 3.10 or later. Includes typed parameters and response dictionaries. This package is an alpha release.

## Installation

```sh
python -m pip install --pre smspva-sdk
# Or pin this release:
python -m pip install smspva-sdk==0.1.0a2
```

## API coverage

The SDK provides 56 methods across three APIs:

| API | Methods | Use it to |
| --- | --- | --- |
| Activation V2 | 20 | Request a number, check availability and receive verification SMS. |
| Rental | 22 | Manage [phone number rentals](https://smspva.com/rent) and retrieve messages for existing orders. |
| Private Email | 14 | Check providers and services, manage [private email rentals](https://smspva.com/rent-mail.html), and read incoming messages. |

Country, service and provider lists come from the live API. Availability and prices can change. Alternative API is not included.

## Quickstart

[Sign in to your SMSPVA account](https://smspva.com/signin.html) and open **Profile and ApiKey** from the account menu. Set the key as the **SMSPVA_API_KEY** environment variable before running a protected request. Keep it on your server and out of source control.

The examples below read your balance and reference data; they do not create an order.

### Synchronous client

```python
import os
from smspva import SMSPVA

with SMSPVA(os.environ["SMSPVA_API_KEY"]) as client:
    print(client.activation.get_balance())
    print(client.rental.get_countries())
    print(client.email.get_providers())
```

### Asynchronous client

```python
import asyncio
import os
from smspva import AsyncSMSPVA

async def main():
    async with AsyncSMSPVA(os.environ["SMSPVA_API_KEY"]) as client:
        result = await client.activation.get_balance()
        print(result)

asyncio.run(main())
```

Use the client as a context manager, or call `close()` / `await aclose()` yourself. Async uses HTTPX `AsyncClient`, not worker threads.

## Requests and results

- Activation V2 sends the key in the `apikey` header. Rental and Email use the `apikey` query parameter. Public methods send no key or cookies. Optional-key rental methods use the client key unless you pass `use_api_key=False`.
- Returned dictionaries preserve wire field names and values, including string prices, timestamps, and IDs. Types follow the source schemas; a field not marked required remains optional.
- `is_pending(result)` recognises Activation SMS HTTP 202 / `SMS_NOT_YET_RECEIVED`. `is_no_stock(result)` recognises Email creation `status=2`. Both return the original response instead of raising a generic error.
- All documented optional parameters are available, including `partnerkey`, `partner_key`, `provider`, `extend`, pagination and search. Query and path values are encoded. Email `pcode=None` or `pcode=""` is omitted entirely.
- `rental.get_multi_service_count` requires explicit `dtype` and `dcount` because the docs warn that backend defaults are unreliable. The wire method remains `get_count_multi`.

```python
# Public reference data, without an API key.
with SMSPVA() as client:
    services = client.email.get_data(pcode="CODE_FROM_GET_PROVIDERS")
```

Paid example (run only when you intend to create a rental):

```python
from smspva import is_no_stock

with SMSPVA(os.environ["SMSPVA_API_KEY"]) as client:
    result = client.email.create_order(
        scode="CODE_FROM_GET_DATA", dtype="week", dcount=1
    )
    if is_no_stock(result):
        print("No mailbox available; refresh counts before trying again.")
    else:
        print(result)
```

## Waiting for SMS

Save an expiry once when the number is created. `wait_for_sms` polls only Receive SMS, never creates another order, and stops on terminal errors, expiry or a transport failure. A new SMS retrieval can trigger payment.

```python
import time

# number_result is the successful response from your own get_number request.
expires_at = time.time() + number_result["data"]["orderExpireIn"]
result = client.activation.wait_for_sms(
    orderid=number_result["data"]["orderId"], expires_at=expires_at
)
```

Use `await client.activation.wait_for_sms(...)` with `AsyncSMSPVA`. The helper waits at least five seconds between pending responses; this is a helper policy, not a claim about an API-wide rate limit. Request deadlines are bounded by the saved expiry. HTTPX timeouts apply to individual network operations; the async polling helper also enforces an overall remaining deadline.

## Errors and timeouts

`ApiError` retains `family`, `operation`, `http_status`, `code` and the original `response`. `ProtocolError` means the body was not a usable JSON envelope. `TransportError` and `RequestTimeoutError` mean the request outcome may be unknown (`outcome_unknown` for state-changing/paid methods). No requests are retried automatically; inspect current orders before repeating a paid operation.

Exception messages omit request URLs and keys. Query credentials may still appear if you enable HTTPX request logging; redact those logs. Do not put account keys in browser code.

The default timeout is 30 seconds per HTTPX network operation. Override at client construction or per call with `timeout=...`. Advanced transports, proxies and test doubles can be supplied through `transport=httpx.HTTPTransport(...)` or `httpx.AsyncHTTPTransport(...)`; environment proxies/cookies are not inherited. Redirects are never followed.

The generated method index is in `METHODS.md`. Response TypedDicts and input aliases are available in `smspva.types`; the package includes `py.typed`.

## Development

To build from source and run the local checks:

```sh
git clone https://github.com/SMSPVA/smspva-python.git
cd smspva-python
python -m pip install -e . build mypy
python -m unittest discover -s tests -v
python -m mypy
python -m build
```

Tests use synthetic fixtures and local transports; they do not buy numbers or call the production API.

## Documentation and support

Read the [SMSPVA API documentation](https://docs.smspva.com/) for endpoint parameters, response codes and the activation, rental and email workflows. The [method index](https://github.com/SMSPVA/smspva-python/blob/main/METHODS.md) maps every SDK method to its API operation.

For account, billing or service questions, visit the [SMSPVA help center](https://smspva.com/help.html). Report SDK bugs through this repository's issues, without API keys or private message content.

## License

MIT. See [LICENSE](https://github.com/SMSPVA/smspva-python/blob/main/LICENSE).
