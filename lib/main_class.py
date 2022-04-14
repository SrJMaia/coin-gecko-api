from lib.cg_api_status.main_api_status import get_status_from_api
from lib.cg_api_simple.main_api_simple import get_simple_price_from_api

class PyGecko():

    __API_URL = "https://api.coingecko.com/api/v3/"
    
    def __init__(self):
        return


    def get_status(self, return_status_code = False):
        return get_status_from_api(self.__API_URL, 
                                    return_status = return_status_code)

    def get_simple_price(self,
                        crypto_list,
                        second_currency_list=["usd"],
                        market_cap=False,
                        last_24_vol=False,
                        last_24_change=False,
                        last_update_at=False,
                        return_status_code = False):
        return get_simple_price_from_api(self.__API_URL,
                                    return_status = return_status_code,
                                    cryptos_list=crypto_list,
                                    second_currency_list=second_currency_list,
                                    market_cap=market_cap,
                                    last_24_vol=last_24_vol,
                                    last_24_change=last_24_change,
                                    last_update_at=last_update_at
        )