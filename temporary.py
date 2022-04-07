from pygecko import PyGecko

x = PyGecko()

print(x.get_status())
print(x.get_status(return_status_code=True))
print(x.get_simple_price(crypto_list=["bitcoin"]))
print(x.get_simple_price(crypto_list=["bitcoin"], return_status_code=True))
