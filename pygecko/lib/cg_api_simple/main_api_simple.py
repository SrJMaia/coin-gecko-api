from pygecko.lib.global_functions import bytes_to_dict
import requests
import json

def get_simple_price_from_api(url,
                            cryptos_list,
                            return_status,
                            second_currency_list=["usd"],
                            market_cap=False,
                            last_24_vol=False,
                            last_24_change=False,
                            last_update_at=False,):
    """
    
    Paramaters
    ----------
        url (str): The API url.
        cryptos (list): A list of strings with the crypto's name.
        second_currency (list): a list of strings with the second pair.
            default ['usd'].
    """

    url += "simple/price?"

    url = f"{url}ids={'%2C%20'.join(cryptos_list).lower().strip()}"

    url = f"{url}&vs_currencies={'%2C'.join(second_currency_list).lower().strip()}"

    url = f"{url}&include_market_cap={market_cap}"

    url = f"{url}&include_24hr_vol={last_24_vol}"

    url = f"{url}&include_24hr_change={last_24_change}"

    url = f"{url}&include_last_updated_at={last_update_at}"

    url = url.lower()

    r = requests.get(url)

    return bytes_to_dict(r, return_status)



