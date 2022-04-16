import requests
import json

def get_status_from_api(url):
    """
    Get the current API status.

    Paramaters
    ----------
        url (str): The API url.

    Return
    ------
        status (dict): The API responde.
    """

    url += "ping"

    r = requests.get(url)

    return json.loads(r.content)