import requests
import ast

def get_status_from_api(url):
    """
    Get the current API status and the respective message.

    Paramaters
        url (str): The API url.

    Return
        status (dict)
    """

    url += "ping"

    r = requests.get(url)

    status_code = r.status_code
    status = ast.literal_eval(r.content.decode("utf-8"))

    status["status_code"] = status_code

    return status