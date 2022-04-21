import main_api_simple as mps
import unittest

class TestPyGecko(unittest.TestCase):

    URL = "https://api.coingecko.com/api/v3/"
    BTC_USD_PRICE = 39284
    BTC_EUR_PRICE = 36429
    BTC_MARKET_CAP = 746431916789
    BTC_VOL = 25087513458
    BTC_PCT_CHANGE = -2.94


    # API TESTS
    def test_api_simple_v1(self):
        actual = mps.get_simple_price_from_api(url=self.URL, 
                                            cryptos_list=["bitcoin"])
        expected = {"bitcoin":{"usd":self.BTC_USD_PRICE}}
        self.assertEqual(actual, expected)

    """
    For prices, I use a fix value since that doesn't change and the accuracy
    is easier to measure. With market cap and volume, I used the difference
    where if the difference is higher than 1% the test will fail.
    The volume and market cap from CoinGecko website is different from the api.
    """

    def test_api_simple_v2(self):
        actual = mps.get_simple_price_from_api(url=self.URL, 
                                            cryptos_list=["bitcoin"],
                                            second_currency_list=["usd","eur"])
        expected = {"bitcoin":{"usd": self.BTC_USD_PRICE, 
                                "eur":self.BTC_EUR_PRICE}}
        self.assertEqual(actual, expected)

    def test_api_simple_v3(self):
        actual = mps.get_simple_price_from_api(url=self.URL, 
                                            cryptos_list=["bitcoin"],
                                            market_cap=True)
        expected = (self.BTC_MARKET_CAP / actual["bitcoin"]["usd_market_cap"] - 1) * 100
        self.assertLess(expected, 0.95, 2)

    def test_api_simple_v4(self):
        actual = mps.get_simple_price_from_api(url=self.URL, 
                                            cryptos_list=["bitcoin"],
                                            last_24_vol=True)
        expected = (self.BTC_VOL / actual["bitcoin"]["usd_24h_vol"] - 1) * 100
        self.assertLess(expected, 1., 2)

    def test_api_simple_v5(self):
        actual = mps.get_simple_price_from_api(url=self.URL, 
                                            cryptos_list=["bitcoin"],
                                            last_24_change=True)
        expected = {"bitcoin":{"usd": self.BTC_USD_PRICE,
                                "usd_24h_change":self.BTC_PCT_CHANGE}}
        actual["bitcoin"]["usd_24h_change"] = round(actual["bitcoin"]["usd_24h_change"], 2)
        self.assertEqual(actual, expected)


    # WEB SCRAPING TESTS
    def test_get_circulating_supply_v1(self):
        actual = mps.get_circulating_supply("bitcoin")
        expected = 19015975
        self.assertEqual(actual, expected)

    def test_get_circulating_supply_v2(self):
        actual = mps.get_circulating_supply("cronos")
        expected = 25263013692
        self.assertEqual(actual, expected)

    def test_get_total_supply_v1(self):
        actual = mps.get_total_supply("bitcoin")
        expected = 21000000
        self.assertEqual(actual, expected)

    def test_get_total_supply_v2(self):
        actual = mps.get_total_supply("cronos")
        expected = 30263013692
        self.assertEqual(actual, expected)
    
    def test_get_total_supply_v3(self):
        actual = mps.get_total_supply("ethereum")
        expected = None
        self.assertEqual(actual, expected)

    def test_get_max_supply_v1(self):
        actual = mps.get_max_supply("bitcoin")
        expected = 21000000
        self.assertEqual(actual, expected)

    def test_get_max_supply_v2(self):
        actual = mps.get_max_supply("cronos")
        expected = None
        self.assertEqual(actual, expected)
    
    def test_get_max_supply_v3(self):
        actual = mps.get_max_supply("ethereum")
        expected = None
        self.assertEqual(actual, expected)