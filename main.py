from cg_api_status.main_api_status import get_status_from_api

class CoinGeckoAPI():

    __API_URL = "https://api.coingecko.com/api/v3/"
    
    def __init__(self):
        pass

    def get_status(self):
        return get_status_from_api(self.__API_URL)
    


x = CoinGeckoAPI()

print(x.get_status())
