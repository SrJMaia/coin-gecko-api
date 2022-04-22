try:  # For tests
    from cg_api_status import get_status_from_api
    from cg_api_simple import get_supported_vs_currencies_api, get_simple_price_from_api
except:  # For external import
    from .cg_api_status import get_status_from_api
    from .cg_api_simple import (
        get_supported_vs_currencies_api,
        get_simple_price_from_api,
    )


class PyGecko:

    __API_URL = "https://api.coingecko.com/api/v3/"

    def __init__(self):
        return

    # Status
    @classmethod
    def get_status(self):
        return get_status_from_api(self.__API_URL)

    # Simple
    @classmethod
    def get_simple_price(
        self,
        crypto_list,
        second_currency_list=["usd"],
        market_cap=False,
        last_24_vol=False,
        last_24_change=False,
        last_update_at=False,
        supply=False,
    ):
        return get_simple_price_from_api(
            self.__API_URL,
            cryptos_list=crypto_list,
            second_currency_list=second_currency_list,
            market_cap=market_cap,
            last_24_vol=last_24_vol,
            last_24_change=last_24_change,
            last_update_at=last_update_at,
            supply=supply,
        )

    @classmethod
    def get_vs_currencies(self):
        return get_supported_vs_currencies_api(self.__API_URL)
