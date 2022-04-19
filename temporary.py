from pygecko import PyGecko

x = PyGecko()

print(x.get_status())
print(x.get_simple_price(crypto_list=["basic-attention-token"]))
print(x.get_simple_price(crypto_list=["bitcoin"], second_currency_list=["usd","eur"]))
print(x.get_simple_price(crypto_list=["bitcoin","ethereum"]))
print(x.get_simple_price(crypto_list=["bitcoin"], supply=True))
print(x.get_simple_price(crypto_list=["solana"], supply=True))
print(x.get_simple_price(crypto_list=["ethereum","bitcoin","dogecoin"], supply=True))
print(x.get_simple_price(crypto_list=["bitcoin"], market_cap=True))
print(x.get_simple_price(crypto_list=["bitcoin"], market_cap=True, last_24_vol=True))
print(x.get_simple_price(crypto_list=["bitcoin"], market_cap=True, last_24_vol=True, last_24_change=True))
print(x.get_simple_price(crypto_list=["bitcoin"], market_cap=True, last_24_vol=True, last_24_change=True, last_update_at=True))
