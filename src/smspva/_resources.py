# Generated named methods; wire names remain unchanged.
from __future__ import annotations
from typing import cast
from . import types as T
from ._transport import Transport, AsyncTransport
from ._polling import wait_for_sms, async_wait_for_sms

class Activation:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_balance(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetBalanceResponse:
        """Get balance. GET /activation/balance"""
        return cast(T.ActivationGetBalanceResponse, self._transport.request("activation.getBalance", {}, timeout=timeout, use_api_key=use_api_key))

    def get_user_info(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetUserInfoResponse:
        """User information. GET /activation/userinfo"""
        return cast(T.ActivationGetUserInfoResponse, self._transport.request("activation.getUserInfo", {}, timeout=timeout, use_api_key=use_api_key))

    def get_operators(self, *, country: T.ActivationGetOperatorsCountryInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetOperatorsResponse:
        """Operators. GET /activation/operators/{country}"""
        return cast(T.ActivationGetOperatorsResponse, self._transport.request("activation.getOperators", {"country": country}, timeout=timeout, use_api_key=use_api_key))

    def get_conversions(self, *, service: T.ActivationGetConversionsServiceInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetConversionsResponse:
        """Conversion rates. GET /activation/conversions/{service}"""
        return cast(T.ActivationGetConversionsResponse, self._transport.request("activation.getConversions", {"service": service}, timeout=timeout, use_api_key=use_api_key))

    def get_message_type_settings(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetMessageTypeSettingsResponse:
        """Message type settings. GET /activation/countryservicesettings"""
        return cast(T.ActivationGetMessageTypeSettingsResponse, self._transport.request("activation.getMessageTypeSettings", {}, timeout=timeout, use_api_key=use_api_key))

    def get_all_number_counts(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetAllNumberCountsResponse:
        """All number counts. GET /activation/countnumbers"""
        return cast(T.ActivationGetAllNumberCountsResponse, self._transport.request("activation.getAllNumberCounts", {}, timeout=timeout, use_api_key=use_api_key))

    def get_country_number_counts(self, *, country: T.ActivationGetCountryNumberCountsCountryInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetCountryNumberCountsResponse:
        """Country number counts. GET /activation/countnumbers/{country}"""
        return cast(T.ActivationGetCountryNumberCountsResponse, self._transport.request("activation.getCountryNumberCounts", {"country": country}, timeout=timeout, use_api_key=use_api_key))

    def get_service_price(self, *, country: T.ActivationGetServicePriceCountryInput, service: T.ActivationGetServicePriceServiceInput, voice: T.ActivationGetServicePriceVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetServicePriceResponse:
        """Service price. GET /activation/serviceprice/{country}/{service}"""
        return cast(T.ActivationGetServicePriceResponse, self._transport.request("activation.getServicePrice", {"country": country, "service": service, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    def get_country_operator_prices(self, *, country: T.ActivationGetCountryOperatorPricesCountryInput, voice: T.ActivationGetCountryOperatorPricesVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetCountryOperatorPricesResponse:
        """Country operator prices. GET /activation/serviceprice/{country}"""
        return cast(T.ActivationGetCountryOperatorPricesResponse, self._transport.request("activation.getCountryOperatorPrices", {"country": country, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    def get_service_prices(self, *, service: T.ActivationGetServicePricesServiceInput, voice: T.ActivationGetServicePricesVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetServicePricesResponse:
        """Service prices by country. GET /activation/serviceprices/{service}"""
        return cast(T.ActivationGetServicePricesResponse, self._transport.request("activation.getServicePrices", {"service": service, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    def get_all_service_prices(self, *, voice: T.ActivationGetAllServicePricesVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetAllServicePricesResponse:
        """All service prices. GET /activation/servicesprices"""
        return cast(T.ActivationGetAllServicePricesResponse, self._transport.request("activation.getAllServicePrices", {"voice": voice}, timeout=timeout, use_api_key=use_api_key))

    def get_number(self, *, country: T.ActivationGetNumberCountryInput, service: T.ActivationGetNumberServiceInput, voice: T.ActivationGetNumberVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetNumberResponse:
        """Get number. GET /activation/number/{country}/{service}"""
        return cast(T.ActivationGetNumberResponse, self._transport.request("activation.getNumber", {"country": country, "service": service, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    def get_number_by_operator(self, *, country: T.ActivationGetNumberByOperatorCountryInput, service: T.ActivationGetNumberByOperatorServiceInput, operator: T.ActivationGetNumberByOperatorOperatorInput, voice: T.ActivationGetNumberByOperatorVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetNumberByOperatorResponse:
        """Get number by operator. GET /activation/number/{country}/{service}/{operator}"""
        return cast(T.ActivationGetNumberByOperatorResponse, self._transport.request("activation.getNumberByOperator", {"country": country, "service": service, "operator": operator, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    def receive_sms(self, *, partnerkey: T.ActivationReceiveSmsPartnerkeyInput | None = None, orderid: T.ActivationReceiveSmsOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationReceiveSmsResponseResult:
        """Receive SMS. GET /activation/sms/{orderid}"""
        return cast(T.ActivationReceiveSmsResponseResult, self._transport.request("activation.receiveSms", {"partnerkey": partnerkey, "orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    def get_orders(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetOrdersResponse:
        """Current orders. GET /activation/orders"""
        return cast(T.ActivationGetOrdersResponse, self._transport.request("activation.getOrders", {}, timeout=timeout, use_api_key=use_api_key))

    def get_number_status(self, *, number: T.ActivationGetNumberStatusNumberInput, service: T.ActivationGetNumberStatusServiceInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetNumberStatusResponse:
        """Number status. GET /activation/numberstatus/{number}/{service}"""
        return cast(T.ActivationGetNumberStatusResponse, self._transport.request("activation.getNumberStatus", {"number": number, "service": service}, timeout=timeout, use_api_key=use_api_key))

    def clear_sms(self, *, orderid: T.ActivationClearSmsOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationClearSmsResponse:
        """Clear SMS. PUT /activation/clearsms/{orderid}"""
        return cast(T.ActivationClearSmsResponse, self._transport.request("activation.clearSms", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    def stop_sms(self, *, orderid: T.ActivationStopSmsOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationStopSmsResponse:
        """Stop SMS. PUT /activation/stopsms/{orderid}"""
        return cast(T.ActivationStopSmsResponse, self._transport.request("activation.stopSms", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    def cancel_order(self, *, orderid: T.ActivationCancelOrderOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationCancelOrderResponse:
        """Cancel order. PUT /activation/cancelorder/{orderid}"""
        return cast(T.ActivationCancelOrderResponse, self._transport.request("activation.cancelOrder", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    def block_number(self, *, orderid: T.ActivationBlockNumberOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationBlockNumberResponse:
        """Block number. PUT /activation/blocknumber/{orderid}"""
        return cast(T.ActivationBlockNumberResponse, self._transport.request("activation.blockNumber", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    def wait_for_sms(self, *, orderid: int, expires_at: float, interval: float = 5.0, partnerkey: str | None = None) -> T.ActivationReceiveSmsResponse:
        return cast(T.ActivationReceiveSmsResponse, wait_for_sms(self._transport, orderid, expires_at, interval, partnerkey))

class AsyncActivation:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_balance(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetBalanceResponse:
        """Get balance. GET /activation/balance"""
        return cast(T.ActivationGetBalanceResponse, await self._transport.request("activation.getBalance", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_user_info(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetUserInfoResponse:
        """User information. GET /activation/userinfo"""
        return cast(T.ActivationGetUserInfoResponse, await self._transport.request("activation.getUserInfo", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_operators(self, *, country: T.ActivationGetOperatorsCountryInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetOperatorsResponse:
        """Operators. GET /activation/operators/{country}"""
        return cast(T.ActivationGetOperatorsResponse, await self._transport.request("activation.getOperators", {"country": country}, timeout=timeout, use_api_key=use_api_key))

    async def get_conversions(self, *, service: T.ActivationGetConversionsServiceInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetConversionsResponse:
        """Conversion rates. GET /activation/conversions/{service}"""
        return cast(T.ActivationGetConversionsResponse, await self._transport.request("activation.getConversions", {"service": service}, timeout=timeout, use_api_key=use_api_key))

    async def get_message_type_settings(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetMessageTypeSettingsResponse:
        """Message type settings. GET /activation/countryservicesettings"""
        return cast(T.ActivationGetMessageTypeSettingsResponse, await self._transport.request("activation.getMessageTypeSettings", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_all_number_counts(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetAllNumberCountsResponse:
        """All number counts. GET /activation/countnumbers"""
        return cast(T.ActivationGetAllNumberCountsResponse, await self._transport.request("activation.getAllNumberCounts", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_country_number_counts(self, *, country: T.ActivationGetCountryNumberCountsCountryInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetCountryNumberCountsResponse:
        """Country number counts. GET /activation/countnumbers/{country}"""
        return cast(T.ActivationGetCountryNumberCountsResponse, await self._transport.request("activation.getCountryNumberCounts", {"country": country}, timeout=timeout, use_api_key=use_api_key))

    async def get_service_price(self, *, country: T.ActivationGetServicePriceCountryInput, service: T.ActivationGetServicePriceServiceInput, voice: T.ActivationGetServicePriceVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetServicePriceResponse:
        """Service price. GET /activation/serviceprice/{country}/{service}"""
        return cast(T.ActivationGetServicePriceResponse, await self._transport.request("activation.getServicePrice", {"country": country, "service": service, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    async def get_country_operator_prices(self, *, country: T.ActivationGetCountryOperatorPricesCountryInput, voice: T.ActivationGetCountryOperatorPricesVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetCountryOperatorPricesResponse:
        """Country operator prices. GET /activation/serviceprice/{country}"""
        return cast(T.ActivationGetCountryOperatorPricesResponse, await self._transport.request("activation.getCountryOperatorPrices", {"country": country, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    async def get_service_prices(self, *, service: T.ActivationGetServicePricesServiceInput, voice: T.ActivationGetServicePricesVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetServicePricesResponse:
        """Service prices by country. GET /activation/serviceprices/{service}"""
        return cast(T.ActivationGetServicePricesResponse, await self._transport.request("activation.getServicePrices", {"service": service, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    async def get_all_service_prices(self, *, voice: T.ActivationGetAllServicePricesVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetAllServicePricesResponse:
        """All service prices. GET /activation/servicesprices"""
        return cast(T.ActivationGetAllServicePricesResponse, await self._transport.request("activation.getAllServicePrices", {"voice": voice}, timeout=timeout, use_api_key=use_api_key))

    async def get_number(self, *, country: T.ActivationGetNumberCountryInput, service: T.ActivationGetNumberServiceInput, voice: T.ActivationGetNumberVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetNumberResponse:
        """Get number. GET /activation/number/{country}/{service}"""
        return cast(T.ActivationGetNumberResponse, await self._transport.request("activation.getNumber", {"country": country, "service": service, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    async def get_number_by_operator(self, *, country: T.ActivationGetNumberByOperatorCountryInput, service: T.ActivationGetNumberByOperatorServiceInput, operator: T.ActivationGetNumberByOperatorOperatorInput, voice: T.ActivationGetNumberByOperatorVoiceInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetNumberByOperatorResponse:
        """Get number by operator. GET /activation/number/{country}/{service}/{operator}"""
        return cast(T.ActivationGetNumberByOperatorResponse, await self._transport.request("activation.getNumberByOperator", {"country": country, "service": service, "operator": operator, "voice": voice}, timeout=timeout, use_api_key=use_api_key))

    async def receive_sms(self, *, partnerkey: T.ActivationReceiveSmsPartnerkeyInput | None = None, orderid: T.ActivationReceiveSmsOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationReceiveSmsResponseResult:
        """Receive SMS. GET /activation/sms/{orderid}"""
        return cast(T.ActivationReceiveSmsResponseResult, await self._transport.request("activation.receiveSms", {"partnerkey": partnerkey, "orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    async def get_orders(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetOrdersResponse:
        """Current orders. GET /activation/orders"""
        return cast(T.ActivationGetOrdersResponse, await self._transport.request("activation.getOrders", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_number_status(self, *, number: T.ActivationGetNumberStatusNumberInput, service: T.ActivationGetNumberStatusServiceInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationGetNumberStatusResponse:
        """Number status. GET /activation/numberstatus/{number}/{service}"""
        return cast(T.ActivationGetNumberStatusResponse, await self._transport.request("activation.getNumberStatus", {"number": number, "service": service}, timeout=timeout, use_api_key=use_api_key))

    async def clear_sms(self, *, orderid: T.ActivationClearSmsOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationClearSmsResponse:
        """Clear SMS. PUT /activation/clearsms/{orderid}"""
        return cast(T.ActivationClearSmsResponse, await self._transport.request("activation.clearSms", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    async def stop_sms(self, *, orderid: T.ActivationStopSmsOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationStopSmsResponse:
        """Stop SMS. PUT /activation/stopsms/{orderid}"""
        return cast(T.ActivationStopSmsResponse, await self._transport.request("activation.stopSms", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    async def cancel_order(self, *, orderid: T.ActivationCancelOrderOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationCancelOrderResponse:
        """Cancel order. PUT /activation/cancelorder/{orderid}"""
        return cast(T.ActivationCancelOrderResponse, await self._transport.request("activation.cancelOrder", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    async def block_number(self, *, orderid: T.ActivationBlockNumberOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.ActivationBlockNumberResponse:
        """Block number. PUT /activation/blocknumber/{orderid}"""
        return cast(T.ActivationBlockNumberResponse, await self._transport.request("activation.blockNumber", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    async def wait_for_sms(self, *, orderid: int, expires_at: float, interval: float = 5.0, partnerkey: str | None = None) -> T.ActivationReceiveSmsResponse:
        return cast(T.ActivationReceiveSmsResponse, await async_wait_for_sms(self._transport, orderid, expires_at, interval, partnerkey))

class Rental:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_countries(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCountriesResponse:
        """Rental countries. GET /api/rent.php?method=getcountries"""
        return cast(T.RentalGetCountriesResponse, self._transport.request("rental.getCountries", {}, timeout=timeout, use_api_key=use_api_key))

    def get_default_services(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetDefaultServicesResponse:
        """Default services. GET /api/rent.php?method=get_default_services"""
        return cast(T.RentalGetDefaultServicesResponse, self._transport.request("rental.getDefaultServices", {}, timeout=timeout, use_api_key=use_api_key))

    def get_countries_by_service(self, *, service: T.RentalGetCountriesByServiceServiceInput, dtype: T.RentalGetCountriesByServiceDtypeInput, dcount: T.RentalGetCountriesByServiceDcountInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCountriesByServiceResponse:
        """Countries by service. GET /api/rent.php?method=get_country_by_service"""
        return cast(T.RentalGetCountriesByServiceResponse, self._transport.request("rental.getCountriesByService", {"service": service, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    def get_data(self, *, country: T.RentalGetDataCountryInput, dtype: T.RentalGetDataDtypeInput | None = None, dcount: T.RentalGetDataDcountInput | None = None, extend: T.RentalGetDataExtendInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetDataResponse:
        """Rental data. GET /api/rent.php?method=getdata"""
        return cast(T.RentalGetDataResponse, self._transport.request("rental.getData", {"country": country, "dtype": dtype, "dcount": dcount, "extend": extend}, timeout=timeout, use_api_key=use_api_key))

    def get_data_with_providers(self, *, country: T.RentalGetDataWithProvidersCountryInput, dtype: T.RentalGetDataWithProvidersDtypeInput | None = None, dcount: T.RentalGetDataWithProvidersDcountInput | None = None, extend: T.RentalGetDataWithProvidersExtendInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetDataWithProvidersResponse:
        """Rental data by provider. GET /api/rent.php?method=getdataWithProviders"""
        return cast(T.RentalGetDataWithProvidersResponse, self._transport.request("rental.getDataWithProviders", {"country": country, "dtype": dtype, "dcount": dcount, "extend": extend}, timeout=timeout, use_api_key=use_api_key))

    def get_count(self, *, country: T.RentalGetCountCountryInput, dtype: T.RentalGetCountDtypeInput | None = None, dcount: T.RentalGetCountDcountInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCountResponse:
        """Available number counts. GET /api/rent.php?method=getcount"""
        return cast(T.RentalGetCountResponse, self._transport.request("rental.getCount", {"country": country, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    def get_count_with_providers(self, *, country: T.RentalGetCountWithProvidersCountryInput, dtype: T.RentalGetCountWithProvidersDtypeInput | None = None, dcount: T.RentalGetCountWithProvidersDcountInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCountWithProvidersResponse:
        """Counts by provider. GET /api/rent.php?method=getCountWithProviders"""
        return cast(T.RentalGetCountWithProvidersResponse, self._transport.request("rental.getCountWithProviders", {"country": country, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    def get_multi_service_count(self, *, country: T.RentalGetMultiServiceCountCountryInput, services: T.RentalGetMultiServiceCountServicesInput, dtype: T.RentalGetMultiServiceCountDtypeInput, dcount: T.RentalGetMultiServiceCountDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetMultiServiceCountResponse:
        """Multi-service count. GET /api/rent.php?method=get_count_multi"""
        return cast(T.RentalGetMultiServiceCountResponse, self._transport.request("rental.getMultiServiceCount", {"country": country, "services": services, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    def get_canada_paypal_days(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCanadaPaypalDaysResponse:
        """Canada PayPal days. GET /api/rent.php?method=get_days_canada_paypal"""
        return cast(T.RentalGetCanadaPaypalDaysResponse, self._transport.request("rental.getCanadaPaypalDays", {}, timeout=timeout, use_api_key=use_api_key))

    def get_minimum_paypal_days(self, *, country: T.RentalGetMinimumPaypalDaysCountryInput, service: T.RentalGetMinimumPaypalDaysServiceInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetMinimumPaypalDaysResponse:
        """Minimum PayPal days. GET /api/rent.php?method=get_min_paypal_days"""
        return cast(T.RentalGetMinimumPaypalDaysResponse, self._transport.request("rental.getMinimumPaypalDays", {"country": country, "service": service}, timeout=timeout, use_api_key=use_api_key))

    def create(self, *, dtype: T.RentalCreateDtypeInput, dcount: T.RentalCreateDcountInput, country: T.RentalCreateCountryInput, service: T.RentalCreateServiceInput, provider: T.RentalCreateProviderInput | None = None, partner_key: T.RentalCreatePartner_keyInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalCreateResponse:
        """Create rental. GET /api/rent.php?method=create"""
        return cast(T.RentalCreateResponse, self._transport.request("rental.create", {"dtype": dtype, "dcount": dcount, "country": country, "service": service, "provider": provider, "partner_key": partner_key}, timeout=timeout, use_api_key=use_api_key))

    def create_multi(self, *, dtype: T.RentalCreateMultiDtypeInput, dcount: T.RentalCreateMultiDcountInput, country: T.RentalCreateMultiCountryInput, services: T.RentalCreateMultiServicesInput, provider: T.RentalCreateMultiProviderInput | None = None, partner_key: T.RentalCreateMultiPartner_keyInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalCreateMultiResponse:
        """Create multi-service rental. GET /api/rent.php?method=create_multi"""
        return cast(T.RentalCreateMultiResponse, self._transport.request("rental.createMulti", {"dtype": dtype, "dcount": dcount, "country": country, "services": services, "provider": provider, "partner_key": partner_key}, timeout=timeout, use_api_key=use_api_key))

    def add_service_to_order(self, *, id: T.RentalAddServiceToOrderIdInput, service: T.RentalAddServiceToOrderServiceInput, pnumber: T.RentalAddServiceToOrderPnumberInput, rent_days: T.RentalAddServiceToOrderRent_daysInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalAddServiceToOrderResponse:
        """Add service to order. GET /api/rent.php?method=add_service_to_order"""
        return cast(T.RentalAddServiceToOrderResponse, self._transport.request("rental.addServiceToOrder", {"id": id, "service": service, "pnumber": pnumber, "rent_days": rent_days}, timeout=timeout, use_api_key=use_api_key))

    def get_orders(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetOrdersResponse:
        """Rental orders. GET /api/rent.php?method=orders"""
        return cast(T.RentalGetOrdersResponse, self._transport.request("rental.getOrders", {}, timeout=timeout, use_api_key=use_api_key))

    def activate(self, *, id: T.RentalActivateIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalActivateResponse:
        """Activate rental. GET /api/rent.php?method=activate"""
        return cast(T.RentalActivateResponse, self._transport.request("rental.activate", {"id": id}, timeout=timeout, use_api_key=use_api_key))

    def get_sms(self, *, id: T.RentalGetSmsIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetSmsResponse:
        """Rental SMS. GET /api/rent.php?method=sms"""
        return cast(T.RentalGetSmsResponse, self._transport.request("rental.getSms", {"id": id}, timeout=timeout, use_api_key=use_api_key))

    def prolong(self, *, id: T.RentalProlongIdInput, dtype: T.RentalProlongDtypeInput, dcount: T.RentalProlongDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalProlongResponse:
        """Prolong rental. GET /api/rent.php?method=prolong"""
        return cast(T.RentalProlongResponse, self._transport.request("rental.prolong", {"id": id, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    def prolong_by_days(self, *, id: T.RentalProlongByDaysIdInput, dtype: T.RentalProlongByDaysDtypeInput, dcount: T.RentalProlongByDaysDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalProlongByDaysResponse:
        """Prolong by days. GET /api/rent.php?method=prolong_max"""
        return cast(T.RentalProlongByDaysResponse, self._transport.request("rental.prolongByDays", {"id": id, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    def delete_order(self, *, id: T.RentalDeleteOrderIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalDeleteOrderResponse:
        """Remove order. GET /api/rent.php?method=delete"""
        return cast(T.RentalDeleteOrderResponse, self._transport.request("rental.deleteOrder", {"id": id}, timeout=timeout, use_api_key=use_api_key))

    def get_history(self, *, skip: T.RentalGetHistorySkipInput | None = None, take: T.RentalGetHistoryTakeInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetHistoryResponse:
        """Rental history. GET /api/rent.php?method=get_rent_history"""
        return cast(T.RentalGetHistoryResponse, self._transport.request("rental.getHistory", {"skip": skip, "take": take}, timeout=timeout, use_api_key=use_api_key))

    def get_restore_cost(self, *, id: T.RentalGetRestoreCostIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetRestoreCostResponse:
        """Restore precalculation. GET /api/rent.php?method=restore_user_precalc"""
        return cast(T.RentalGetRestoreCostResponse, self._transport.request("rental.getRestoreCost", {"id": id}, timeout=timeout, use_api_key=use_api_key))

    def restore(self, *, id: T.RentalRestoreIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalRestoreResponse:
        """Restore rental. GET /api/rent.php?method=restore_user"""
        return cast(T.RentalRestoreResponse, self._transport.request("rental.restore", {"id": id}, timeout=timeout, use_api_key=use_api_key))

class AsyncRental:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_countries(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCountriesResponse:
        """Rental countries. GET /api/rent.php?method=getcountries"""
        return cast(T.RentalGetCountriesResponse, await self._transport.request("rental.getCountries", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_default_services(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetDefaultServicesResponse:
        """Default services. GET /api/rent.php?method=get_default_services"""
        return cast(T.RentalGetDefaultServicesResponse, await self._transport.request("rental.getDefaultServices", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_countries_by_service(self, *, service: T.RentalGetCountriesByServiceServiceInput, dtype: T.RentalGetCountriesByServiceDtypeInput, dcount: T.RentalGetCountriesByServiceDcountInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCountriesByServiceResponse:
        """Countries by service. GET /api/rent.php?method=get_country_by_service"""
        return cast(T.RentalGetCountriesByServiceResponse, await self._transport.request("rental.getCountriesByService", {"service": service, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    async def get_data(self, *, country: T.RentalGetDataCountryInput, dtype: T.RentalGetDataDtypeInput | None = None, dcount: T.RentalGetDataDcountInput | None = None, extend: T.RentalGetDataExtendInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetDataResponse:
        """Rental data. GET /api/rent.php?method=getdata"""
        return cast(T.RentalGetDataResponse, await self._transport.request("rental.getData", {"country": country, "dtype": dtype, "dcount": dcount, "extend": extend}, timeout=timeout, use_api_key=use_api_key))

    async def get_data_with_providers(self, *, country: T.RentalGetDataWithProvidersCountryInput, dtype: T.RentalGetDataWithProvidersDtypeInput | None = None, dcount: T.RentalGetDataWithProvidersDcountInput | None = None, extend: T.RentalGetDataWithProvidersExtendInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetDataWithProvidersResponse:
        """Rental data by provider. GET /api/rent.php?method=getdataWithProviders"""
        return cast(T.RentalGetDataWithProvidersResponse, await self._transport.request("rental.getDataWithProviders", {"country": country, "dtype": dtype, "dcount": dcount, "extend": extend}, timeout=timeout, use_api_key=use_api_key))

    async def get_count(self, *, country: T.RentalGetCountCountryInput, dtype: T.RentalGetCountDtypeInput | None = None, dcount: T.RentalGetCountDcountInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCountResponse:
        """Available number counts. GET /api/rent.php?method=getcount"""
        return cast(T.RentalGetCountResponse, await self._transport.request("rental.getCount", {"country": country, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    async def get_count_with_providers(self, *, country: T.RentalGetCountWithProvidersCountryInput, dtype: T.RentalGetCountWithProvidersDtypeInput | None = None, dcount: T.RentalGetCountWithProvidersDcountInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCountWithProvidersResponse:
        """Counts by provider. GET /api/rent.php?method=getCountWithProviders"""
        return cast(T.RentalGetCountWithProvidersResponse, await self._transport.request("rental.getCountWithProviders", {"country": country, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    async def get_multi_service_count(self, *, country: T.RentalGetMultiServiceCountCountryInput, services: T.RentalGetMultiServiceCountServicesInput, dtype: T.RentalGetMultiServiceCountDtypeInput, dcount: T.RentalGetMultiServiceCountDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetMultiServiceCountResponse:
        """Multi-service count. GET /api/rent.php?method=get_count_multi"""
        return cast(T.RentalGetMultiServiceCountResponse, await self._transport.request("rental.getMultiServiceCount", {"country": country, "services": services, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    async def get_canada_paypal_days(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetCanadaPaypalDaysResponse:
        """Canada PayPal days. GET /api/rent.php?method=get_days_canada_paypal"""
        return cast(T.RentalGetCanadaPaypalDaysResponse, await self._transport.request("rental.getCanadaPaypalDays", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_minimum_paypal_days(self, *, country: T.RentalGetMinimumPaypalDaysCountryInput, service: T.RentalGetMinimumPaypalDaysServiceInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetMinimumPaypalDaysResponse:
        """Minimum PayPal days. GET /api/rent.php?method=get_min_paypal_days"""
        return cast(T.RentalGetMinimumPaypalDaysResponse, await self._transport.request("rental.getMinimumPaypalDays", {"country": country, "service": service}, timeout=timeout, use_api_key=use_api_key))

    async def create(self, *, dtype: T.RentalCreateDtypeInput, dcount: T.RentalCreateDcountInput, country: T.RentalCreateCountryInput, service: T.RentalCreateServiceInput, provider: T.RentalCreateProviderInput | None = None, partner_key: T.RentalCreatePartner_keyInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalCreateResponse:
        """Create rental. GET /api/rent.php?method=create"""
        return cast(T.RentalCreateResponse, await self._transport.request("rental.create", {"dtype": dtype, "dcount": dcount, "country": country, "service": service, "provider": provider, "partner_key": partner_key}, timeout=timeout, use_api_key=use_api_key))

    async def create_multi(self, *, dtype: T.RentalCreateMultiDtypeInput, dcount: T.RentalCreateMultiDcountInput, country: T.RentalCreateMultiCountryInput, services: T.RentalCreateMultiServicesInput, provider: T.RentalCreateMultiProviderInput | None = None, partner_key: T.RentalCreateMultiPartner_keyInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalCreateMultiResponse:
        """Create multi-service rental. GET /api/rent.php?method=create_multi"""
        return cast(T.RentalCreateMultiResponse, await self._transport.request("rental.createMulti", {"dtype": dtype, "dcount": dcount, "country": country, "services": services, "provider": provider, "partner_key": partner_key}, timeout=timeout, use_api_key=use_api_key))

    async def add_service_to_order(self, *, id: T.RentalAddServiceToOrderIdInput, service: T.RentalAddServiceToOrderServiceInput, pnumber: T.RentalAddServiceToOrderPnumberInput, rent_days: T.RentalAddServiceToOrderRent_daysInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalAddServiceToOrderResponse:
        """Add service to order. GET /api/rent.php?method=add_service_to_order"""
        return cast(T.RentalAddServiceToOrderResponse, await self._transport.request("rental.addServiceToOrder", {"id": id, "service": service, "pnumber": pnumber, "rent_days": rent_days}, timeout=timeout, use_api_key=use_api_key))

    async def get_orders(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetOrdersResponse:
        """Rental orders. GET /api/rent.php?method=orders"""
        return cast(T.RentalGetOrdersResponse, await self._transport.request("rental.getOrders", {}, timeout=timeout, use_api_key=use_api_key))

    async def activate(self, *, id: T.RentalActivateIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalActivateResponse:
        """Activate rental. GET /api/rent.php?method=activate"""
        return cast(T.RentalActivateResponse, await self._transport.request("rental.activate", {"id": id}, timeout=timeout, use_api_key=use_api_key))

    async def get_sms(self, *, id: T.RentalGetSmsIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetSmsResponse:
        """Rental SMS. GET /api/rent.php?method=sms"""
        return cast(T.RentalGetSmsResponse, await self._transport.request("rental.getSms", {"id": id}, timeout=timeout, use_api_key=use_api_key))

    async def prolong(self, *, id: T.RentalProlongIdInput, dtype: T.RentalProlongDtypeInput, dcount: T.RentalProlongDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalProlongResponse:
        """Prolong rental. GET /api/rent.php?method=prolong"""
        return cast(T.RentalProlongResponse, await self._transport.request("rental.prolong", {"id": id, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    async def prolong_by_days(self, *, id: T.RentalProlongByDaysIdInput, dtype: T.RentalProlongByDaysDtypeInput, dcount: T.RentalProlongByDaysDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalProlongByDaysResponse:
        """Prolong by days. GET /api/rent.php?method=prolong_max"""
        return cast(T.RentalProlongByDaysResponse, await self._transport.request("rental.prolongByDays", {"id": id, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    async def delete_order(self, *, id: T.RentalDeleteOrderIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalDeleteOrderResponse:
        """Remove order. GET /api/rent.php?method=delete"""
        return cast(T.RentalDeleteOrderResponse, await self._transport.request("rental.deleteOrder", {"id": id}, timeout=timeout, use_api_key=use_api_key))

    async def get_history(self, *, skip: T.RentalGetHistorySkipInput | None = None, take: T.RentalGetHistoryTakeInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetHistoryResponse:
        """Rental history. GET /api/rent.php?method=get_rent_history"""
        return cast(T.RentalGetHistoryResponse, await self._transport.request("rental.getHistory", {"skip": skip, "take": take}, timeout=timeout, use_api_key=use_api_key))

    async def get_restore_cost(self, *, id: T.RentalGetRestoreCostIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalGetRestoreCostResponse:
        """Restore precalculation. GET /api/rent.php?method=restore_user_precalc"""
        return cast(T.RentalGetRestoreCostResponse, await self._transport.request("rental.getRestoreCost", {"id": id}, timeout=timeout, use_api_key=use_api_key))

    async def restore(self, *, id: T.RentalRestoreIdInput, timeout: float | None = None, use_api_key: bool = True) -> T.RentalRestoreResponse:
        """Restore rental. GET /api/rent.php?method=restore_user"""
        return cast(T.RentalRestoreResponse, await self._transport.request("rental.restore", {"id": id}, timeout=timeout, use_api_key=use_api_key))

class Email:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_providers(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetProvidersResponse:
        """Providers. GET /api/rent_email.php?method=get_providers"""
        return cast(T.EmailGetProvidersResponse, self._transport.request("email.getProviders", {}, timeout=timeout, use_api_key=use_api_key))

    def get_data(self, *, pcode: T.EmailGetDataPcodeInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetDataResponse:
        """Services & prices. GET /api/rent_email.php?method=get_data"""
        return cast(T.EmailGetDataResponse, self._transport.request("email.getData", {"pcode": pcode}, timeout=timeout, use_api_key=use_api_key))

    def get_count(self, *, pcode: T.EmailGetCountPcodeInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetCountResponse:
        """Mailbox counts. GET /api/rent_email.php?method=get_count"""
        return cast(T.EmailGetCountResponse, self._transport.request("email.getCount", {"pcode": pcode}, timeout=timeout, use_api_key=use_api_key))

    def create_order(self, *, scode: T.EmailCreateOrderScodeInput, pcode: T.EmailCreateOrderPcodeInput | None = None, dtype: T.EmailCreateOrderDtypeInput, dcount: T.EmailCreateOrderDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailCreateOrderResponse:
        """Create rental. GET /api/rent_email.php?method=create_order"""
        return cast(T.EmailCreateOrderResponse, self._transport.request("email.createOrder", {"scode": scode, "pcode": pcode, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    def get_orders(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetOrdersResponse:
        """Active orders. GET /api/rent_email.php?method=get_orders"""
        return cast(T.EmailGetOrdersResponse, self._transport.request("email.getOrders", {}, timeout=timeout, use_api_key=use_api_key))

    def get_mails(self, *, orderid: T.EmailGetMailsOrderidInput, t: T.EmailGetMailsTInput | None = None, s: T.EmailGetMailsSInput | None = None, sq: T.EmailGetMailsSqInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetMailsResponse:
        """List messages. GET /api/rent_email.php?method=get_mails"""
        return cast(T.EmailGetMailsResponse, self._transport.request("email.getMails", {"orderid": orderid, "t": t, "s": s, "sq": sq}, timeout=timeout, use_api_key=use_api_key))

    def get_mail_body(self, *, orderid: T.EmailGetMailBodyOrderidInput, emailid: T.EmailGetMailBodyEmailidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetMailBodyResponse:
        """Message body. GET /api/rent_email.php?method=get_mail_body"""
        return cast(T.EmailGetMailBodyResponse, self._transport.request("email.getMailBody", {"orderid": orderid, "emailid": emailid}, timeout=timeout, use_api_key=use_api_key))

    def buy_alias(self, *, orderid: T.EmailBuyAliasOrderidInput, aliasid: T.EmailBuyAliasAliasidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailBuyAliasResponse:
        """Buy alias access. GET /api/rent_email.php?method=buy_alias"""
        return cast(T.EmailBuyAliasResponse, self._transport.request("email.buyAlias", {"orderid": orderid, "aliasid": aliasid}, timeout=timeout, use_api_key=use_api_key))

    def get_mails_by_alias(self, *, orderid: T.EmailGetMailsByAliasOrderidInput, aliasid: T.EmailGetMailsByAliasAliasidInput, t: T.EmailGetMailsByAliasTInput | None = None, s: T.EmailGetMailsByAliasSInput | None = None, sq: T.EmailGetMailsByAliasSqInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetMailsByAliasResponse:
        """Alias messages. GET /api/rent_email.php?method=get_mails_by_alias"""
        return cast(T.EmailGetMailsByAliasResponse, self._transport.request("email.getMailsByAlias", {"orderid": orderid, "aliasid": aliasid, "t": t, "s": s, "sq": sq}, timeout=timeout, use_api_key=use_api_key))

    def prolong_order(self, *, orderid: T.EmailProlongOrderOrderidInput, dtype: T.EmailProlongOrderDtypeInput, dcount: T.EmailProlongOrderDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailProlongOrderResponse:
        """Extend rental. GET /api/rent_email.php?method=prolong_order"""
        return cast(T.EmailProlongOrderResponse, self._transport.request("email.prolongOrder", {"orderid": orderid, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    def cancel_order(self, *, orderid: T.EmailCancelOrderOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailCancelOrderResponse:
        """Cancel rental. GET /api/rent_email.php?method=cancel_order"""
        return cast(T.EmailCancelOrderResponse, self._transport.request("email.cancelOrder", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    def get_archived_orders(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetArchivedOrdersResponse:
        """Archived orders. GET /api/rent_email.php?method=get_archived_orders"""
        return cast(T.EmailGetArchivedOrdersResponse, self._transport.request("email.getArchivedOrders", {}, timeout=timeout, use_api_key=use_api_key))

    def calc_restore_order(self, *, orderid: T.EmailCalcRestoreOrderOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailCalcRestoreOrderResponse:
        """Restoration cost. GET /api/rent_email.php?method=calc_restore_order"""
        return cast(T.EmailCalcRestoreOrderResponse, self._transport.request("email.calcRestoreOrder", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    def restore_order(self, *, orderid: T.EmailRestoreOrderOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailRestoreOrderResponse:
        """Restore rental. GET /api/rent_email.php?method=restore_order"""
        return cast(T.EmailRestoreOrderResponse, self._transport.request("email.restoreOrder", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

class AsyncEmail:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_providers(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetProvidersResponse:
        """Providers. GET /api/rent_email.php?method=get_providers"""
        return cast(T.EmailGetProvidersResponse, await self._transport.request("email.getProviders", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_data(self, *, pcode: T.EmailGetDataPcodeInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetDataResponse:
        """Services & prices. GET /api/rent_email.php?method=get_data"""
        return cast(T.EmailGetDataResponse, await self._transport.request("email.getData", {"pcode": pcode}, timeout=timeout, use_api_key=use_api_key))

    async def get_count(self, *, pcode: T.EmailGetCountPcodeInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetCountResponse:
        """Mailbox counts. GET /api/rent_email.php?method=get_count"""
        return cast(T.EmailGetCountResponse, await self._transport.request("email.getCount", {"pcode": pcode}, timeout=timeout, use_api_key=use_api_key))

    async def create_order(self, *, scode: T.EmailCreateOrderScodeInput, pcode: T.EmailCreateOrderPcodeInput | None = None, dtype: T.EmailCreateOrderDtypeInput, dcount: T.EmailCreateOrderDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailCreateOrderResponse:
        """Create rental. GET /api/rent_email.php?method=create_order"""
        return cast(T.EmailCreateOrderResponse, await self._transport.request("email.createOrder", {"scode": scode, "pcode": pcode, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    async def get_orders(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetOrdersResponse:
        """Active orders. GET /api/rent_email.php?method=get_orders"""
        return cast(T.EmailGetOrdersResponse, await self._transport.request("email.getOrders", {}, timeout=timeout, use_api_key=use_api_key))

    async def get_mails(self, *, orderid: T.EmailGetMailsOrderidInput, t: T.EmailGetMailsTInput | None = None, s: T.EmailGetMailsSInput | None = None, sq: T.EmailGetMailsSqInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetMailsResponse:
        """List messages. GET /api/rent_email.php?method=get_mails"""
        return cast(T.EmailGetMailsResponse, await self._transport.request("email.getMails", {"orderid": orderid, "t": t, "s": s, "sq": sq}, timeout=timeout, use_api_key=use_api_key))

    async def get_mail_body(self, *, orderid: T.EmailGetMailBodyOrderidInput, emailid: T.EmailGetMailBodyEmailidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetMailBodyResponse:
        """Message body. GET /api/rent_email.php?method=get_mail_body"""
        return cast(T.EmailGetMailBodyResponse, await self._transport.request("email.getMailBody", {"orderid": orderid, "emailid": emailid}, timeout=timeout, use_api_key=use_api_key))

    async def buy_alias(self, *, orderid: T.EmailBuyAliasOrderidInput, aliasid: T.EmailBuyAliasAliasidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailBuyAliasResponse:
        """Buy alias access. GET /api/rent_email.php?method=buy_alias"""
        return cast(T.EmailBuyAliasResponse, await self._transport.request("email.buyAlias", {"orderid": orderid, "aliasid": aliasid}, timeout=timeout, use_api_key=use_api_key))

    async def get_mails_by_alias(self, *, orderid: T.EmailGetMailsByAliasOrderidInput, aliasid: T.EmailGetMailsByAliasAliasidInput, t: T.EmailGetMailsByAliasTInput | None = None, s: T.EmailGetMailsByAliasSInput | None = None, sq: T.EmailGetMailsByAliasSqInput | None = None, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetMailsByAliasResponse:
        """Alias messages. GET /api/rent_email.php?method=get_mails_by_alias"""
        return cast(T.EmailGetMailsByAliasResponse, await self._transport.request("email.getMailsByAlias", {"orderid": orderid, "aliasid": aliasid, "t": t, "s": s, "sq": sq}, timeout=timeout, use_api_key=use_api_key))

    async def prolong_order(self, *, orderid: T.EmailProlongOrderOrderidInput, dtype: T.EmailProlongOrderDtypeInput, dcount: T.EmailProlongOrderDcountInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailProlongOrderResponse:
        """Extend rental. GET /api/rent_email.php?method=prolong_order"""
        return cast(T.EmailProlongOrderResponse, await self._transport.request("email.prolongOrder", {"orderid": orderid, "dtype": dtype, "dcount": dcount}, timeout=timeout, use_api_key=use_api_key))

    async def cancel_order(self, *, orderid: T.EmailCancelOrderOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailCancelOrderResponse:
        """Cancel rental. GET /api/rent_email.php?method=cancel_order"""
        return cast(T.EmailCancelOrderResponse, await self._transport.request("email.cancelOrder", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    async def get_archived_orders(self, *, timeout: float | None = None, use_api_key: bool = True) -> T.EmailGetArchivedOrdersResponse:
        """Archived orders. GET /api/rent_email.php?method=get_archived_orders"""
        return cast(T.EmailGetArchivedOrdersResponse, await self._transport.request("email.getArchivedOrders", {}, timeout=timeout, use_api_key=use_api_key))

    async def calc_restore_order(self, *, orderid: T.EmailCalcRestoreOrderOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailCalcRestoreOrderResponse:
        """Restoration cost. GET /api/rent_email.php?method=calc_restore_order"""
        return cast(T.EmailCalcRestoreOrderResponse, await self._transport.request("email.calcRestoreOrder", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

    async def restore_order(self, *, orderid: T.EmailRestoreOrderOrderidInput, timeout: float | None = None, use_api_key: bool = True) -> T.EmailRestoreOrderResponse:
        """Restore rental. GET /api/rent_email.php?method=restore_order"""
        return cast(T.EmailRestoreOrderResponse, await self._transport.request("email.restoreOrder", {"orderid": orderid}, timeout=timeout, use_api_key=use_api_key))

