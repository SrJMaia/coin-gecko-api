from lib import PyGecko
import unittest

class TestPyGecko(unittest.TestCase):

    def test_api_status_without_status_code(self):
        actual = PyGecko().get_status()
        expected = {"gecko_says": "(V3 To the Moon!)"}
        self.assertEqual(actual, expected)