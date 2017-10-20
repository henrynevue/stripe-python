import stripe
from stripe.test.helper import StripeResourceTest


class ExchangeRatesTest(StripeResourceTest):

    def test_exchange_rates_list(self):
        stripe.ExchangeRates.list()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/exchange_rates',
            {}
        )

    def test_exchange_rates_retrieve(self):
        stripe.ExchangeRates.retrieve('usd')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/exchange_rates/usd',
            {},
            None
        )
