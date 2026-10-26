"""Static consumer checks; these functions never run as part of unit tests."""
from typing_extensions import assert_type

from smspva import SMSPVA, AsyncSMSPVA, is_no_stock, is_pending
from smspva.types import (
    ActivationPending,
    ActivationReceiveSmsResponse,
    EmailCreateOrderResponseVariant0,
    EmailCreateOrderResponseVariant1,
)


def consume_sync(client: SMSPVA) -> None:
    order = client.email.create_order(scode="service-code", dtype="day", dcount=1)
    if is_no_stock(order):
        assert_type(order, EmailCreateOrderResponseVariant1)
    else:
        assert_type(order, EmailCreateOrderResponseVariant0)
        print(order["data"])

    sms = client.activation.receive_sms(orderid=1)
    if is_pending(sms):
        assert_type(sms, ActivationPending)
    else:
        assert_type(sms, ActivationReceiveSmsResponse)
        print(sms["data"])


async def consume_async(client: AsyncSMSPVA) -> None:
    order = await client.email.create_order(scode="service-code", dtype="day", dcount=1)
    if not is_no_stock(order):
        assert_type(order, EmailCreateOrderResponseVariant0)
        print(order["data"])
    else:
        assert_type(order, EmailCreateOrderResponseVariant1)

    sms = await client.activation.receive_sms(orderid=1)
    if not is_pending(sms):
        assert_type(sms, ActivationReceiveSmsResponse)
        print(sms["data"])
    else:
        assert_type(sms, ActivationPending)
