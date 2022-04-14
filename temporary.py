from lib import PyGecko

x = PyGecko()

print(x.get_status())
print(x.get_status(return_status_code=True))
print(x.get_simple_price(crypto_list=["bitcoin"]))
print(x.get_simple_price(crypto_list=["bitcoin"], return_status_code=True))
print(x.get_simple_price(crypto_list=["bitcoin"], market_cap=True,return_status_code=True))
print(x.get_simple_price(crypto_list=["bitcoin"], market_cap=True, last_24_vol=True, last_24_change=True, last_update_at=True,return_status_code=True))
