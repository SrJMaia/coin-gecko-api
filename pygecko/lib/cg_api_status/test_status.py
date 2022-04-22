from status import get_status_from_api
import unittest


class TestStatus(unittest.TestCase):
    def test_api_status_without_status_code(self):
        url = "https://api.coingecko.com/api/v3/"
        actual = get_status_from_api(url=url)
        expected = {"gecko_says": "(V3) To the Moon!"}
        self.assertEqual(actual, expected)
