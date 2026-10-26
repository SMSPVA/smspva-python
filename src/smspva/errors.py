"""SDK errors do not embed request URLs or credentials in their messages."""
from typing import Any


class SMSPVAError(Exception):
    pass


class ValidationError(SMSPVAError, ValueError):
    pass


class ApiError(SMSPVAError):
    def __init__(self, family: str, operation: str, http_status: int, code: str | int, response: dict[str, Any]):
        self.family, self.operation, self.http_status = family, operation, http_status
        self.code, self.response = code, response
        super().__init__(f"SMSPVA {family} request failed (HTTP {http_status})")


class ProtocolError(SMSPVAError):
    def __init__(self, family: str, operation: str, http_status: int):
        self.family, self.operation, self.http_status = family, operation, http_status
        super().__init__(f"SMSPVA {family} returned an invalid response (HTTP {http_status})")


class TransportError(SMSPVAError):
    def __init__(self, family: str, operation: str, outcome_unknown: bool, kind: str = "network"):
        self.family, self.operation = family, operation
        self.outcome_unknown, self.kind = outcome_unknown, kind
        super().__init__(f"SMSPVA {family} request {kind}; no automatic retry")


class RequestTimeoutError(TransportError):
    pass


class PollingTimeoutError(SMSPVAError):
    def __init__(self) -> None:
        super().__init__("No SMS result before the saved order deadline")
