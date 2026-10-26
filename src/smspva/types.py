# Generated from docs/data. Edit sdk/scripts/generate.mjs.
from typing import Any, Literal, TypeAlias, TypedDict
from typing_extensions import Required, NotRequired

ActivationPending = TypedDict("ActivationPending", {"statusCode": Literal[202], "error": dict[str, Any]})

ActivationGetBalanceResponseData = TypedDict("ActivationGetBalanceResponseData", {"balance": NotRequired[str]}, total=False)

ActivationGetBalanceResponse = TypedDict("ActivationGetBalanceResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetBalanceResponseData]}, total=False)


ActivationGetUserInfoResponseData = TypedDict("ActivationGetUserInfoResponseData", {"balance": NotRequired[str], "name": NotRequired[str], "karma": NotRequired[float]}, total=False)

ActivationGetUserInfoResponse = TypedDict("ActivationGetUserInfoResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetUserInfoResponseData]}, total=False)


ActivationGetOperatorsResponseData = TypedDict("ActivationGetOperatorsResponseData", {"country": NotRequired[str], "operators": NotRequired[list[str]]}, total=False)

ActivationGetOperatorsResponse = TypedDict("ActivationGetOperatorsResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetOperatorsResponseData]}, total=False)

ActivationGetOperatorsCountryInput: TypeAlias = str

ActivationGetConversionsResponseData = TypedDict("ActivationGetConversionsResponseData", {"service": NotRequired[str], "conversions": NotRequired[dict[str, int]]}, total=False)

ActivationGetConversionsResponse = TypedDict("ActivationGetConversionsResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetConversionsResponseData]}, total=False)

ActivationGetConversionsServiceInput: TypeAlias = str

ActivationGetMessageTypeSettingsResponseDataItem = TypedDict("ActivationGetMessageTypeSettingsResponseDataItem", {"country": Required[str], "service": Required[str], "operator": Required[str], "voice": Required[Literal[0, 1]], "caller": Required[Literal[0, 1]], "sms": Required[Literal[0, 1]]}, total=False)

ActivationGetMessageTypeSettingsResponse = TypedDict("ActivationGetMessageTypeSettingsResponse", {"statusCode": Required[Literal[200]], "data": Required[list[ActivationGetMessageTypeSettingsResponseDataItem]]}, total=False)


ActivationGetAllNumberCountsResponseDataItemServicesItem = TypedDict("ActivationGetAllNumberCountsResponseDataItemServicesItem", {"service": NotRequired[str], "total": NotRequired[int]}, total=False)

ActivationGetAllNumberCountsResponseDataItem = TypedDict("ActivationGetAllNumberCountsResponseDataItem", {"operator": NotRequired[str], "country": NotRequired[str], "services": NotRequired[list[ActivationGetAllNumberCountsResponseDataItemServicesItem]]}, total=False)

ActivationGetAllNumberCountsResponse = TypedDict("ActivationGetAllNumberCountsResponse", {"statusCode": NotRequired[int], "data": NotRequired[list[ActivationGetAllNumberCountsResponseDataItem]]}, total=False)


ActivationGetCountryNumberCountsResponseDataItemServicesItem = TypedDict("ActivationGetCountryNumberCountsResponseDataItemServicesItem", {"service": NotRequired[str], "total": NotRequired[int]}, total=False)

ActivationGetCountryNumberCountsResponseDataItem = TypedDict("ActivationGetCountryNumberCountsResponseDataItem", {"operator": NotRequired[str], "country": NotRequired[str], "services": NotRequired[list[ActivationGetCountryNumberCountsResponseDataItemServicesItem]]}, total=False)

ActivationGetCountryNumberCountsResponse = TypedDict("ActivationGetCountryNumberCountsResponse", {"statusCode": NotRequired[int], "data": NotRequired[list[ActivationGetCountryNumberCountsResponseDataItem]]}, total=False)

ActivationGetCountryNumberCountsCountryInput: TypeAlias = str

ActivationGetServicePriceResponseData = TypedDict("ActivationGetServicePriceResponseData", {"service": NotRequired[str], "serviceDescription": NotRequired[str], "country": NotRequired[str], "price": NotRequired[str], "priceByOperators": NotRequired[dict[str, str]]}, total=False)

ActivationGetServicePriceResponse = TypedDict("ActivationGetServicePriceResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetServicePriceResponseData]}, total=False)

ActivationGetServicePriceCountryInput: TypeAlias = str
ActivationGetServicePriceServiceInput: TypeAlias = str
ActivationGetServicePriceVoiceInput: TypeAlias = Literal[0, 1, 2]

ActivationGetCountryOperatorPricesResponseDataItem = TypedDict("ActivationGetCountryOperatorPricesResponseDataItem", {"s": NotRequired[str], "sd": NotRequired[str], "c": NotRequired[str], "p": NotRequired[str], "po": NotRequired[dict[str, str]]}, total=False)

ActivationGetCountryOperatorPricesResponse = TypedDict("ActivationGetCountryOperatorPricesResponse", {"statusCode": NotRequired[int], "data": NotRequired[list[ActivationGetCountryOperatorPricesResponseDataItem]]}, total=False)

ActivationGetCountryOperatorPricesCountryInput: TypeAlias = str
ActivationGetCountryOperatorPricesVoiceInput: TypeAlias = Literal[0, 1, 2]

ActivationGetServicePricesResponseDataClistItemOpersItem = TypedDict("ActivationGetServicePricesResponseDataClistItemOpersItem", {"opcode": NotRequired[str], "price": NotRequired[float], "count": NotRequired[int]}, total=False)

ActivationGetServicePricesResponseDataClistItem = TypedDict("ActivationGetServicePricesResponseDataClistItem", {"ccode": NotRequired[str], "cname": NotRequired[str], "opers": NotRequired[list[ActivationGetServicePricesResponseDataClistItemOpersItem]]}, total=False)

ActivationGetServicePricesResponseData = TypedDict("ActivationGetServicePricesResponseData", {"scode": NotRequired[str], "sname": NotRequired[str], "clist": NotRequired[list[ActivationGetServicePricesResponseDataClistItem]]}, total=False)

ActivationGetServicePricesResponse = TypedDict("ActivationGetServicePricesResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetServicePricesResponseData]}, total=False)

ActivationGetServicePricesServiceInput: TypeAlias = str
ActivationGetServicePricesVoiceInput: TypeAlias = Literal[0, 1, 2]

ActivationGetAllServicePricesResponseDataItem = TypedDict("ActivationGetAllServicePricesResponseDataItem", {"service": NotRequired[str], "serviceDescription": NotRequired[str], "country": NotRequired[str], "price": NotRequired[str]}, total=False)

ActivationGetAllServicePricesResponse = TypedDict("ActivationGetAllServicePricesResponse", {"statusCode": NotRequired[int], "data": NotRequired[list[ActivationGetAllServicePricesResponseDataItem]]}, total=False)

ActivationGetAllServicePricesVoiceInput: TypeAlias = Literal[0, 1, 2]

ActivationGetNumberResponseData = TypedDict("ActivationGetNumberResponseData", {"orderId": NotRequired[int], "phoneNumber": NotRequired[int], "countryCode": NotRequired[str], "orderExpireIn": NotRequired[int]}, total=False)

ActivationGetNumberResponse = TypedDict("ActivationGetNumberResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetNumberResponseData]}, total=False)

ActivationGetNumberCountryInput: TypeAlias = str
ActivationGetNumberServiceInput: TypeAlias = str
ActivationGetNumberVoiceInput: TypeAlias = Literal[0, 1, 2]

ActivationGetNumberByOperatorResponseData = TypedDict("ActivationGetNumberByOperatorResponseData", {"orderId": NotRequired[int], "phoneNumber": NotRequired[int], "countryCode": NotRequired[str], "orderExpireIn": NotRequired[int]}, total=False)

ActivationGetNumberByOperatorResponse = TypedDict("ActivationGetNumberByOperatorResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetNumberByOperatorResponseData]}, total=False)

ActivationGetNumberByOperatorCountryInput: TypeAlias = str
ActivationGetNumberByOperatorServiceInput: TypeAlias = str
ActivationGetNumberByOperatorOperatorInput: TypeAlias = str
ActivationGetNumberByOperatorVoiceInput: TypeAlias = Literal[0, 1, 2]

ActivationReceiveSmsResponseDataSms = TypedDict("ActivationReceiveSmsResponseDataSms", {"code": NotRequired[str], "fullText": NotRequired[str]}, total=False)

ActivationReceiveSmsResponseData = TypedDict("ActivationReceiveSmsResponseData", {"sms": NotRequired[ActivationReceiveSmsResponseDataSms], "orderId": NotRequired[int], "orderExpireIn": NotRequired[int]}, total=False)

ActivationReceiveSmsResponse = TypedDict("ActivationReceiveSmsResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationReceiveSmsResponseData]}, total=False)

ActivationReceiveSmsResponseResult: TypeAlias = ActivationReceiveSmsResponse | ActivationPending

ActivationReceiveSmsPartnerkeyInput: TypeAlias = str
ActivationReceiveSmsOrderidInput: TypeAlias = int

ActivationGetOrdersResponseDataOrdersItemSms = TypedDict("ActivationGetOrdersResponseDataOrdersItemSms", {"code": NotRequired[str], "fullText": NotRequired[str]}, total=False)

ActivationGetOrdersResponseDataOrdersItem = TypedDict("ActivationGetOrdersResponseDataOrdersItem", {"orderId": NotRequired[int], "phoneNumber": NotRequired[int], "countryCode": NotRequired[str], "orderExpireIn": NotRequired[int], "service": NotRequired[str], "country": NotRequired[str], "status": NotRequired[str], "sms": NotRequired[ActivationGetOrdersResponseDataOrdersItemSms]}, total=False)

ActivationGetOrdersResponseData = TypedDict("ActivationGetOrdersResponseData", {"orders": NotRequired[list[ActivationGetOrdersResponseDataOrdersItem]]}, total=False)

ActivationGetOrdersResponse = TypedDict("ActivationGetOrdersResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetOrdersResponseData]}, total=False)


ActivationGetNumberStatusResponseData = TypedDict("ActivationGetNumberStatusResponseData", {"number": NotRequired[str], "orderId": NotRequired[int], "countryCode": NotRequired[str]}, total=False)

ActivationGetNumberStatusResponse = TypedDict("ActivationGetNumberStatusResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationGetNumberStatusResponseData]}, total=False)

ActivationGetNumberStatusNumberInput: TypeAlias = str
ActivationGetNumberStatusServiceInput: TypeAlias = str

ActivationClearSmsResponseData = TypedDict("ActivationClearSmsResponseData", {"orderId": NotRequired[int], "orderExpireIn": NotRequired[int]}, total=False)

ActivationClearSmsResponse = TypedDict("ActivationClearSmsResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationClearSmsResponseData]}, total=False)

ActivationClearSmsOrderidInput: TypeAlias = int

ActivationStopSmsResponseData = TypedDict("ActivationStopSmsResponseData", {"orderId": NotRequired[int]}, total=False)

ActivationStopSmsResponse = TypedDict("ActivationStopSmsResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationStopSmsResponseData]}, total=False)

ActivationStopSmsOrderidInput: TypeAlias = int

ActivationCancelOrderResponseData = TypedDict("ActivationCancelOrderResponseData", {"orderId": NotRequired[int]}, total=False)

ActivationCancelOrderResponse = TypedDict("ActivationCancelOrderResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationCancelOrderResponseData]}, total=False)

ActivationCancelOrderOrderidInput: TypeAlias = int

ActivationBlockNumberResponseData = TypedDict("ActivationBlockNumberResponseData", {"orderId": NotRequired[int]}, total=False)

ActivationBlockNumberResponse = TypedDict("ActivationBlockNumberResponse", {"statusCode": NotRequired[int], "data": NotRequired[ActivationBlockNumberResponseData]}, total=False)

ActivationBlockNumberOrderidInput: TypeAlias = int

RentalGetCountriesResponseDataItem = TypedDict("RentalGetCountriesResponseDataItem", {"name": NotRequired[str], "code": NotRequired[str], "url_country_name": NotRequired[str], "rent_switch_type": NotRequired[str], "rent_avail_prolong": NotRequired[str]}, total=False)

RentalGetCountriesResponse = TypedDict("RentalGetCountriesResponse", {"status": NotRequired[int], "data": NotRequired[list[RentalGetCountriesResponseDataItem]]}, total=False)


RentalGetDefaultServicesResponseDataItem = TypedDict("RentalGetDefaultServicesResponseDataItem", {"name": NotRequired[str], "service": NotRequired[str], "priceForDay": NotRequired[str], "img": NotRequired[str], "DAYP": NotRequired[str], "PROC": NotRequired[str]}, total=False)

RentalGetDefaultServicesResponse = TypedDict("RentalGetDefaultServicesResponse", {"status": NotRequired[int], "data": NotRequired[list[RentalGetDefaultServicesResponseDataItem]], "msg": NotRequired[str]}, total=False)


RentalGetCountriesByServiceResponseDataValue = TypedDict("RentalGetCountriesByServiceResponseDataValue", {"service_name": NotRequired[str], "price": NotRequired[str], "procent_days": NotRequired[str], "procent": NotRequired[str], "day_step": NotRequired[str], "country": NotRequired[str], "phoneAmount": NotRequired[int]}, total=False)

RentalGetCountriesByServiceResponse = TypedDict("RentalGetCountriesByServiceResponse", {"status": NotRequired[int], "data": NotRequired[dict[str, RentalGetCountriesByServiceResponseDataValue]], "msg": NotRequired[str]}, total=False)

RentalGetCountriesByServiceServiceInput: TypeAlias = str
RentalGetCountriesByServiceDtypeInput: TypeAlias = str
RentalGetCountriesByServiceDcountInput: TypeAlias = int

RentalGetDataResponseDataServicesItem = TypedDict("RentalGetDataResponseDataServicesItem", {"name": NotRequired[str], "service": NotRequired[str], "price_day": NotRequired[float], "count": NotRequired[int], "img": NotRequired[str], "procent_days": NotRequired[int], "procent": NotRequired[int], "day_step": NotRequired[float]}, total=False)

RentalGetDataResponseData = TypedDict("RentalGetDataResponseData", {"services": NotRequired[list[RentalGetDataResponseDataServicesItem]], "totalAmount": NotRequired[int]}, total=False)

RentalGetDataResponse = TypedDict("RentalGetDataResponse", {"status": NotRequired[int], "data": NotRequired[RentalGetDataResponseData], "msg": NotRequired[str]}, total=False)

RentalGetDataCountryInput: TypeAlias = str
RentalGetDataDtypeInput: TypeAlias = str
RentalGetDataDcountInput: TypeAlias = int
RentalGetDataExtendInput: TypeAlias = str

RentalGetDataWithProvidersResponseDataServicesItem = TypedDict("RentalGetDataWithProvidersResponseDataServicesItem", {"name": NotRequired[str], "service": NotRequired[str], "price_day": NotRequired[float], "img": NotRequired[str], "procent_days": NotRequired[int], "procent": NotRequired[int], "day_step": NotRequired[int], "count": NotRequired[dict[str, int]], "totalCount": NotRequired[int]}, total=False)

RentalGetDataWithProvidersResponseData = TypedDict("RentalGetDataWithProvidersResponseData", {"services": NotRequired[list[RentalGetDataWithProvidersResponseDataServicesItem]], "totalAmount": NotRequired[int], "allOperators": NotRequired[list[str]]}, total=False)

RentalGetDataWithProvidersResponse = TypedDict("RentalGetDataWithProvidersResponse", {"status": NotRequired[int], "data": NotRequired[RentalGetDataWithProvidersResponseData], "msg": NotRequired[str]}, total=False)

RentalGetDataWithProvidersCountryInput: TypeAlias = str
RentalGetDataWithProvidersDtypeInput: TypeAlias = str
RentalGetDataWithProvidersDcountInput: TypeAlias = int
RentalGetDataWithProvidersExtendInput: TypeAlias = str

RentalGetCountResponse = TypedDict("RentalGetCountResponse", {"status": NotRequired[int], "data": NotRequired[dict[str, int] | int], "msg": NotRequired[str]}, total=False)

RentalGetCountCountryInput: TypeAlias = str
RentalGetCountDtypeInput: TypeAlias = str
RentalGetCountDcountInput: TypeAlias = int

RentalGetCountWithProvidersResponseDataValue = TypedDict("RentalGetCountWithProvidersResponseDataValue", {"Amount": NotRequired[dict[str, int]], "Total": NotRequired[int]}, total=False)

RentalGetCountWithProvidersResponse = TypedDict("RentalGetCountWithProvidersResponse", {"status": NotRequired[int], "data": NotRequired[dict[str, RentalGetCountWithProvidersResponseDataValue]], "msg": NotRequired[str]}, total=False)

RentalGetCountWithProvidersCountryInput: TypeAlias = str
RentalGetCountWithProvidersDtypeInput: TypeAlias = str
RentalGetCountWithProvidersDcountInput: TypeAlias = int

RentalGetMultiServiceCountResponseData = TypedDict("RentalGetMultiServiceCountResponseData", {"count": NotRequired[int]}, total=False)

RentalGetMultiServiceCountResponse = TypedDict("RentalGetMultiServiceCountResponse", {"status": NotRequired[int], "data": NotRequired[RentalGetMultiServiceCountResponseData], "msg": NotRequired[str]}, total=False)

RentalGetMultiServiceCountCountryInput: TypeAlias = str
RentalGetMultiServiceCountServicesInput: TypeAlias = str
RentalGetMultiServiceCountDtypeInput: TypeAlias = str
RentalGetMultiServiceCountDcountInput: TypeAlias = int

RentalGetCanadaPaypalDaysResponseDataItem = TypedDict("RentalGetCanadaPaypalDaysResponseDataItem", {"Days": NotRequired[int], "Amount": NotRequired[int]}, total=False)

RentalGetCanadaPaypalDaysResponse = TypedDict("RentalGetCanadaPaypalDaysResponse", {"status": NotRequired[int], "data": NotRequired[list[RentalGetCanadaPaypalDaysResponseDataItem]], "msg": NotRequired[str]}, total=False)


RentalGetMinimumPaypalDaysResponseData = TypedDict("RentalGetMinimumPaypalDaysResponseData", {"Days": NotRequired[int], "Status": NotRequired[int], "Message": NotRequired[str]}, total=False)

RentalGetMinimumPaypalDaysResponse = TypedDict("RentalGetMinimumPaypalDaysResponse", {"status": NotRequired[int], "data": NotRequired[RentalGetMinimumPaypalDaysResponseData], "msg": NotRequired[str]}, total=False)

RentalGetMinimumPaypalDaysCountryInput: TypeAlias = str
RentalGetMinimumPaypalDaysServiceInput: TypeAlias = str

RentalCreateResponseData = TypedDict("RentalCreateResponseData", {"id": NotRequired[int], "pnumber": NotRequired[str], "ccode": NotRequired[str], "service": NotRequired[str], "until": NotRequired[str]}, total=False)

RentalCreateResponse = TypedDict("RentalCreateResponse", {"status": NotRequired[int], "data": NotRequired[RentalCreateResponseData], "msg": NotRequired[str]}, total=False)

RentalCreateDtypeInput: TypeAlias = str
RentalCreateDcountInput: TypeAlias = int
RentalCreateCountryInput: TypeAlias = str
RentalCreateServiceInput: TypeAlias = str
RentalCreateProviderInput: TypeAlias = str
RentalCreatePartner_keyInput: TypeAlias = str

RentalCreateMultiResponseData = TypedDict("RentalCreateMultiResponseData", {"id": NotRequired[int], "pnumber": NotRequired[str], "ccode": NotRequired[str], "service": NotRequired[str], "until": NotRequired[str]}, total=False)

RentalCreateMultiResponse = TypedDict("RentalCreateMultiResponse", {"status": NotRequired[int], "data": NotRequired[RentalCreateMultiResponseData], "msg": NotRequired[str]}, total=False)

RentalCreateMultiDtypeInput: TypeAlias = str
RentalCreateMultiDcountInput: TypeAlias = int
RentalCreateMultiCountryInput: TypeAlias = str
RentalCreateMultiServicesInput: TypeAlias = str
RentalCreateMultiProviderInput: TypeAlias = str
RentalCreateMultiPartner_keyInput: TypeAlias = str

RentalAddServiceToOrderResponseData = TypedDict("RentalAddServiceToOrderResponseData", {"id": NotRequired[int], "pnumber": NotRequired[str], "service": NotRequired[str], "until": NotRequired[int]}, total=False)

RentalAddServiceToOrderResponse = TypedDict("RentalAddServiceToOrderResponse", {"status": NotRequired[int], "data": NotRequired[RentalAddServiceToOrderResponseData]}, total=False)

RentalAddServiceToOrderIdInput: TypeAlias = int
RentalAddServiceToOrderServiceInput: TypeAlias = str
RentalAddServiceToOrderPnumberInput: TypeAlias = str
RentalAddServiceToOrderRent_daysInput: TypeAlias = int

RentalGetOrdersResponseDataItem = TypedDict("RentalGetOrdersResponseDataItem", {"id": NotRequired[int], "scode": NotRequired[str], "sname": NotRequired[str], "state": NotRequired[int], "pnumber": NotRequired[str], "ccode": NotRequired[str], "cname": NotRequired[str], "hasnewsms": NotRequired[bool], "until": NotRequired[int], "canprolong": NotRequired[bool], "canprolongmax": NotRequired[int], "canprolonguntil": NotRequired[int], "lastonline": NotRequired[int]}, total=False)

RentalGetOrdersResponse = TypedDict("RentalGetOrdersResponse", {"status": NotRequired[int], "data": NotRequired[list[RentalGetOrdersResponseDataItem]]}, total=False)


RentalActivateResponseDataItem = TypedDict("RentalActivateResponseDataItem", {"id": NotRequired[int]}, total=False)

RentalActivateResponse = TypedDict("RentalActivateResponse", {"status": NotRequired[int], "data": NotRequired[list[RentalActivateResponseDataItem]]}, total=False)

RentalActivateIdInput: TypeAlias = int

RentalGetSmsResponseDataSmsListItem = TypedDict("RentalGetSmsResponseDataSmsListItem", {"text": NotRequired[str], "sender": NotRequired[str], "date": NotRequired[int]}, total=False)

RentalGetSmsResponseData = TypedDict("RentalGetSmsResponseData", {"SmsList": NotRequired[list[RentalGetSmsResponseDataSmsListItem]], "OtherSms": NotRequired[list[Any]]}, total=False)

RentalGetSmsResponse = TypedDict("RentalGetSmsResponse", {"status": NotRequired[int], "data": NotRequired[RentalGetSmsResponseData]}, total=False)

RentalGetSmsIdInput: TypeAlias = int

RentalProlongResponse = TypedDict("RentalProlongResponse", {"status": NotRequired[int]}, total=False)

RentalProlongIdInput: TypeAlias = int
RentalProlongDtypeInput: TypeAlias = str
RentalProlongDcountInput: TypeAlias = int

RentalProlongByDaysResponse = TypedDict("RentalProlongByDaysResponse", {"status": NotRequired[int]}, total=False)

RentalProlongByDaysIdInput: TypeAlias = int
RentalProlongByDaysDtypeInput: TypeAlias = str
RentalProlongByDaysDcountInput: TypeAlias = int

RentalDeleteOrderResponseData = TypedDict("RentalDeleteOrderResponseData", {"id": NotRequired[int]}, total=False)

RentalDeleteOrderResponse = TypedDict("RentalDeleteOrderResponse", {"status": NotRequired[int], "data": NotRequired[RentalDeleteOrderResponseData], "msg": NotRequired[str]}, total=False)

RentalDeleteOrderIdInput: TypeAlias = int

RentalGetHistoryResponseDataItem = TypedDict("RentalGetHistoryResponseDataItem", {"orderId": NotRequired[int], "resourceCode": NotRequired[str], "number": NotRequired[str], "branchId": NotRequired[int], "haveSms": NotRequired[bool], "isAvailForRestore": NotRequired[bool], "days": NotRequired[int], "country": NotRequired[str], "begin": NotRequired[int], "end": NotRequired[int], "closed": NotRequired[int]}, total=False)

RentalGetHistoryResponse = TypedDict("RentalGetHistoryResponse", {"status": NotRequired[int], "data": NotRequired[list[RentalGetHistoryResponseDataItem]]}, total=False)

RentalGetHistorySkipInput: TypeAlias = int
RentalGetHistoryTakeInput: TypeAlias = int

RentalGetRestoreCostResponseData = TypedDict("RentalGetRestoreCostResponseData", {"ccode": NotRequired[str], "scode": NotRequired[str], "price": NotRequired[float], "sname": NotRequired[str], "pnumber": NotRequired[str], "outdays": NotRequired[int], "orderid": NotRequired[int], "prolongTo": NotRequired[int]}, total=False)

RentalGetRestoreCostResponse = TypedDict("RentalGetRestoreCostResponse", {"status": NotRequired[int], "data": NotRequired[RentalGetRestoreCostResponseData], "msg": NotRequired[str]}, total=False)

RentalGetRestoreCostIdInput: TypeAlias = int

RentalRestoreResponseVariant0Data = TypedDict("RentalRestoreResponseVariant0Data", {"id": Required[int]}, total=False)

RentalRestoreResponseVariant0 = TypedDict("RentalRestoreResponseVariant0", {"status": Required[int], "data": Required[RentalRestoreResponseVariant0Data]}, total=False)

RentalRestoreResponseVariant1 = TypedDict("RentalRestoreResponseVariant1", {"status": Required[int], "msg": Required[str]}, total=False)

RentalRestoreResponse: TypeAlias = RentalRestoreResponseVariant0 | RentalRestoreResponseVariant1

RentalRestoreIdInput: TypeAlias = int

EmailGetProvidersResponseVariant0DataItem = TypedDict("EmailGetProvidersResponseVariant0DataItem", {"id": NotRequired[int], "pcode": NotRequired[str], "name": NotRequired[str]}, total=False)

EmailGetProvidersResponseVariant0 = TypedDict("EmailGetProvidersResponseVariant0", {"status": Required[Literal[1]], "data": Required[list[EmailGetProvidersResponseVariant0DataItem]]}, total=False)

EmailGetProvidersResponse: TypeAlias = EmailGetProvidersResponseVariant0


EmailGetDataResponseVariant0DataItem = TypedDict("EmailGetDataResponseVariant0DataItem", {"count": NotRequired[int], "scode": NotRequired[str], "sname": NotRequired[str], "price": NotRequired[float], "alias_price": NotRequired[float], "icon": NotRequired[str], "months_discount": NotRequired[int]}, total=False)

EmailGetDataResponseVariant0 = TypedDict("EmailGetDataResponseVariant0", {"status": Required[Literal[1]], "data": Required[list[EmailGetDataResponseVariant0DataItem]]}, total=False)

EmailGetDataResponse: TypeAlias = EmailGetDataResponseVariant0

EmailGetDataPcodeInput: TypeAlias = str

EmailGetCountResponseVariant0DataItem = TypedDict("EmailGetCountResponseVariant0DataItem", {"count": NotRequired[int], "scode": NotRequired[str]}, total=False)

EmailGetCountResponseVariant0 = TypedDict("EmailGetCountResponseVariant0", {"status": Required[Literal[1]], "data": Required[list[EmailGetCountResponseVariant0DataItem]]}, total=False)

EmailGetCountResponse: TypeAlias = EmailGetCountResponseVariant0

EmailGetCountPcodeInput: TypeAlias = str

EmailCreateOrderResponseVariant0Data = TypedDict("EmailCreateOrderResponseVariant0Data", {"id": NotRequired[int], "email": NotRequired[str], "scode": NotRequired[str], "pcode": NotRequired[str], "expireDate": NotRequired[int]}, total=False)

EmailCreateOrderResponseVariant0 = TypedDict("EmailCreateOrderResponseVariant0", {"status": Required[Literal[1]], "data": Required[EmailCreateOrderResponseVariant0Data]}, total=False)

EmailCreateOrderResponseVariant1 = TypedDict("EmailCreateOrderResponseVariant1", {"status": Required[Literal[2]]}, total=False)

EmailCreateOrderResponse: TypeAlias = EmailCreateOrderResponseVariant0 | EmailCreateOrderResponseVariant1

EmailCreateOrderScodeInput: TypeAlias = str
EmailCreateOrderPcodeInput: TypeAlias = str
EmailCreateOrderDtypeInput: TypeAlias = Literal["day", "week", "month"]
EmailCreateOrderDcountInput: TypeAlias = int

EmailGetOrdersResponseVariant0DataItemAliasesItem = TypedDict("EmailGetOrdersResponseVariant0DataItemAliasesItem", {"id": NotRequired[int], "address": NotRequired[str], "mesCount": NotRequired[int], "isPaid": NotRequired[bool]}, total=False)

EmailGetOrdersResponseVariant0DataItem = TypedDict("EmailGetOrdersResponseVariant0DataItem", {"id": NotRequired[int], "address": NotRequired[str], "scode": NotRequired[str], "pcode": NotRequired[str], "expireDate": NotRequired[int], "mesCount": NotRequired[int], "aliases": NotRequired[list[EmailGetOrdersResponseVariant0DataItemAliasesItem]], "sname": NotRequired[str]}, total=False)

EmailGetOrdersResponseVariant0 = TypedDict("EmailGetOrdersResponseVariant0", {"status": Required[Literal[1]], "data": Required[list[EmailGetOrdersResponseVariant0DataItem]]}, total=False)

EmailGetOrdersResponse: TypeAlias = EmailGetOrdersResponseVariant0


EmailGetMailsResponseVariant0DataItem = TypedDict("EmailGetMailsResponseVariant0DataItem", {"id": NotRequired[int], "sender": NotRequired[str], "subject": NotRequired[str], "preview": NotRequired[str], "addedAt": NotRequired[str]}, total=False)

EmailGetMailsResponseVariant0 = TypedDict("EmailGetMailsResponseVariant0", {"status": Required[Literal[1]], "data": Required[list[EmailGetMailsResponseVariant0DataItem]]}, total=False)

EmailGetMailsResponse: TypeAlias = EmailGetMailsResponseVariant0

EmailGetMailsOrderidInput: TypeAlias = int
EmailGetMailsTInput: TypeAlias = int
EmailGetMailsSInput: TypeAlias = int
EmailGetMailsSqInput: TypeAlias = str

EmailGetMailBodyResponseVariant0Data = TypedDict("EmailGetMailBodyResponseVariant0Data", {"id": NotRequired[int], "sender": NotRequired[str], "subject": NotRequired[str], "body": NotRequired[str], "addedAt": NotRequired[str]}, total=False)

EmailGetMailBodyResponseVariant0 = TypedDict("EmailGetMailBodyResponseVariant0", {"status": Required[Literal[1]], "data": Required[EmailGetMailBodyResponseVariant0Data]}, total=False)

EmailGetMailBodyResponse: TypeAlias = EmailGetMailBodyResponseVariant0

EmailGetMailBodyOrderidInput: TypeAlias = int
EmailGetMailBodyEmailidInput: TypeAlias = int

EmailBuyAliasResponseVariant0Data = TypedDict("EmailBuyAliasResponseVariant0Data", {"alias": NotRequired[str]}, total=False)

EmailBuyAliasResponseVariant0 = TypedDict("EmailBuyAliasResponseVariant0", {"status": Required[Literal[1]], "data": Required[EmailBuyAliasResponseVariant0Data]}, total=False)

EmailBuyAliasResponse: TypeAlias = EmailBuyAliasResponseVariant0

EmailBuyAliasOrderidInput: TypeAlias = int
EmailBuyAliasAliasidInput: TypeAlias = int

EmailGetMailsByAliasResponseVariant0DataItem = TypedDict("EmailGetMailsByAliasResponseVariant0DataItem", {"id": NotRequired[int], "sender": NotRequired[str], "subject": NotRequired[str], "preview": NotRequired[str], "addedAt": NotRequired[str]}, total=False)

EmailGetMailsByAliasResponseVariant0 = TypedDict("EmailGetMailsByAliasResponseVariant0", {"status": Required[Literal[1]], "data": Required[list[EmailGetMailsByAliasResponseVariant0DataItem]]}, total=False)

EmailGetMailsByAliasResponse: TypeAlias = EmailGetMailsByAliasResponseVariant0

EmailGetMailsByAliasOrderidInput: TypeAlias = int
EmailGetMailsByAliasAliasidInput: TypeAlias = int
EmailGetMailsByAliasTInput: TypeAlias = int
EmailGetMailsByAliasSInput: TypeAlias = int
EmailGetMailsByAliasSqInput: TypeAlias = str

EmailProlongOrderResponseVariant0Data = TypedDict("EmailProlongOrderResponseVariant0Data", {"id": NotRequired[int], "email": NotRequired[str], "service": NotRequired[str]}, total=False)

EmailProlongOrderResponseVariant0 = TypedDict("EmailProlongOrderResponseVariant0", {"status": Required[Literal[1]], "data": Required[EmailProlongOrderResponseVariant0Data]}, total=False)

EmailProlongOrderResponse: TypeAlias = EmailProlongOrderResponseVariant0

EmailProlongOrderOrderidInput: TypeAlias = int
EmailProlongOrderDtypeInput: TypeAlias = Literal["day", "week", "month"]
EmailProlongOrderDcountInput: TypeAlias = int

EmailCancelOrderResponseVariant0 = TypedDict("EmailCancelOrderResponseVariant0", {"status": Required[Literal[1]], "data": Required[bool]}, total=False)

EmailCancelOrderResponse: TypeAlias = EmailCancelOrderResponseVariant0

EmailCancelOrderOrderidInput: TypeAlias = int

EmailGetArchivedOrdersResponseVariant0DataItem = TypedDict("EmailGetArchivedOrdersResponseVariant0DataItem", {"id": NotRequired[int], "address": NotRequired[str], "scode": NotRequired[str], "pcode": NotRequired[str], "expireDate": NotRequired[int], "sname": NotRequired[str]}, total=False)

EmailGetArchivedOrdersResponseVariant0 = TypedDict("EmailGetArchivedOrdersResponseVariant0", {"status": Required[Literal[1]], "data": Required[list[EmailGetArchivedOrdersResponseVariant0DataItem]]}, total=False)

EmailGetArchivedOrdersResponse: TypeAlias = EmailGetArchivedOrdersResponseVariant0


EmailCalcRestoreOrderResponseVariant0 = TypedDict("EmailCalcRestoreOrderResponseVariant0", {"status": Required[Literal[1]], "data": Required[float]}, total=False)

EmailCalcRestoreOrderResponse: TypeAlias = EmailCalcRestoreOrderResponseVariant0

EmailCalcRestoreOrderOrderidInput: TypeAlias = int

EmailRestoreOrderResponseVariant0Data = TypedDict("EmailRestoreOrderResponseVariant0Data", {"id": NotRequired[int], "email": NotRequired[str], "service": NotRequired[str]}, total=False)

EmailRestoreOrderResponseVariant0 = TypedDict("EmailRestoreOrderResponseVariant0", {"status": Required[Literal[1]], "data": Required[EmailRestoreOrderResponseVariant0Data]}, total=False)

EmailRestoreOrderResponse: TypeAlias = EmailRestoreOrderResponseVariant0

EmailRestoreOrderOrderidInput: TypeAlias = int

