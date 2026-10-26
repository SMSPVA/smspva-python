from __future__ import annotations

from types import TracebackType
import httpx

from ._transport import Transport, AsyncTransport
from ._resources import Activation, Rental, Email, AsyncActivation, AsyncRental, AsyncEmail


class SMSPVA:
    def __init__(self, api_key: str | None = None, *, timeout: float = 30, activation_base_url: str | None = None,
                 rental_base_url: str | None = None, email_base_url: str | None = None, transport: httpx.BaseTransport | None = None):
        self._transport = Transport(api_key, timeout, {"activation": activation_base_url, "rental": rental_base_url, "email": email_base_url}, transport)
        self.activation = Activation(self._transport)
        self.rental = Rental(self._transport)
        self.email = Email(self._transport)

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> SMSPVA:
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None:
        self.close()


class AsyncSMSPVA:
    def __init__(self, api_key: str | None = None, *, timeout: float = 30, activation_base_url: str | None = None,
                 rental_base_url: str | None = None, email_base_url: str | None = None, transport: httpx.AsyncBaseTransport | None = None):
        self._transport = AsyncTransport(api_key, timeout, {"activation": activation_base_url, "rental": rental_base_url, "email": email_base_url}, transport)
        self.activation = AsyncActivation(self._transport)
        self.rental = AsyncRental(self._transport)
        self.email = AsyncEmail(self._transport)

    async def aclose(self) -> None:
        await self._transport.close()

    async def __aenter__(self) -> AsyncSMSPVA:
        return self

    async def __aexit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None:
        await self.aclose()
