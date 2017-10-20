from stripe.api_resources.abstract import ListableAPIResource


class ExchangeRates(ListableAPIResource):
    OBJECT_NAME = 'exchange_rates'

    @classmethod
    def class_url(cls):
        return '/v1/exchange_rates'
