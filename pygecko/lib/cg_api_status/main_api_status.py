from pygecko.lib.global_functions import bytes_to_dict
import requests

def get_status_from_api(url, return_status):
    """
    Get the current API status and the respective message.

    Paramaters
        url (str): The API url.

    Return
        status (dict): The API responde and status code.
    """

    url += "ping"

    r = requests.get(url)

    return bytes_to_dict(r, return_status)
