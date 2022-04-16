from main_api_simple import get_simple_price_from_api
import unittest

class TestPyGecko(unittest.TestCase):

    def test_api_simple_v1(self):
        url = "https://api.coingecko.com/api/v3/"
        actual = get_simple_price_from_api(url=url, cryptos_list=["bitcoin"])
        expected = {"gecko_says": "(V3) To the Moon!"}
        self.assertEqual(actual, expected)