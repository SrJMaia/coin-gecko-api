import requests
import json


def get_supported_vs_currencies_api(url):
    """
    Get the current price, marketcap, volume, pct change, last update and supply
    information of any coin supported by the API.

    Paramaters
    ----------
        url (str): The API url.

    Return
    ------
        vs_currencies (list): All supported vs_currencies.
    """

    url += "simple/supported_vs_currencies"

    r = requests.get(url)

    return json.loads(r.content)
