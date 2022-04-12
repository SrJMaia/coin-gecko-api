import json

def bytes_to_dict(request_call, status_code):
    """
    Convert the bytes request to a dict. Return status code if flag is True.

    Paramaters
    ----------
        request_call (bytes): The API request.
        status_code (bool): If True adds the status code into the dict.

    Return
    ------
        request_dict (dict): The API content.
    """

    request_dict = json.loads(request_call.content)

    if status_code:
        request_dict["status_code"] = request_call.status_code
        
    return request_dict