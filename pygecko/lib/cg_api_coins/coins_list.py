import requests
import json


def get_coins_list_from_api(url, include_platform=False):
    """


    Paramaters
    ----------
        url (str): The API url.

    Return
    ------

    """

    url += "coins/list"

    if include_platform:
        url += "&include_platform=True"

    r = requests.get(url)

    return json.loads(r.content)
