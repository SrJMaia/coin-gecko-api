import requests
import json

def get_status_from_api(url):
    """
    Get the current API status and the respective message.

    Paramaters
        url (str): The API url.

    Return
        status (dict): The API responde and status code
    """

    url += "ping"

    r = requests.get(url)

    status = json.loads(r.content)

    status["status_code"] = r.status_code

    return status