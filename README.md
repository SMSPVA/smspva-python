# SMSPVA Python SDK

[![CI](https://github.com/SMSPVA/smspva-python/actions/workflows/ci.yml/badge.svg)](https://github.com/SMSPVA/smspva-python/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) ![Status: alpha](https://img.shields.io/badge/status-alpha-orange.svg)

Python 3.10+, synchronous `SMSPVA` and asynchronous `AsyncSMSPVA`, with the same 56 typed methods. Covers Activation V2 (20), Rental (22) and Private Email (14). Alternative API is excluded. This is an alpha release. PyPI publication is pending.

Install from source:

```sh
git clone https://github.com/SMSPVA/smspva-python.git
cd smspva-python
python -m pip install .
```

```python
import os
from smspva import SMSPVA

with SMSPVA(os.environ["SMSPVA_API_KEY"]) as client:
    print(client.activation.get_balance())
    print(client.rental.get_countries())
    print(client.email.get_providers())
```

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

## License

MIT. See [LICENSE](LICENSE).

## Development

```sh
python -m pip install -e . build mypy
python -m unittest discover -s tests -v
python -m mypy
python -m build
```

Tests use synthetic fixtures and local transports; they do not buy numbers or call the production API.

## Documentation

[API documentation](https://docs.smspva.com)

The new documentation is being prepared in English, Spanish and Chinese. Localized links will be added when it is deployed.

The SDK covers Activation V2, Rental and Private Email. Alternative API is not supported.
