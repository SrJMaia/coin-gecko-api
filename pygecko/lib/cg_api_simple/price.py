from bs4 import BeautifulSoup
from lxml import etree
import requests
import json


def get_simple_price_from_api(
    url,
    cryptos_list,
    second_currency_list=None,
    market_cap=False,
    last_24_vol=False,
    last_24_change=False,
    last_update_at=False,
    supply=False,
):
    """
    Get the current price, marketcap, volume, pct change, last update and supply
    information of any coin supported by the API.

    Paramaters
    ----------
        url (str): The API url.
        cryptos (list): A list of strings with the crypto's name.
        second_currency (list): A list of strings with the second pair.
            default ['usd'].
        market_cap (bool): If True, it will return the market cap of each coin.
                            default False.
        last_24_vol (bool): If True, it will return the last 24h volume of each
                            coin.
                            default False.
        last_24_change (bool): If True, it will return the 24h percent change.
                            default False.
        last_update_at (bool): If True, it will return the last update time in
                            unix time.
                            default False.
        supply (bool): If True, it will return the circulation, total and max
                            supply of the coin.
                            default False.

    Return
    ------
        response_dict (dict): The price and the flag informations from
                            each coin requested.
    """

    if second_currency_list is None:
        second_currency_list = ["usd"]

    url += "simple/price?"

    url = f"{url}ids={'%2C'.join(cryptos_list).lower().strip()}"

    url = f"{url}&vs_currencies={'%2C'.join(second_currency_list).lower().strip()}"

    url = f"{url}&include_market_cap={market_cap}"

    url = f"{url}&include_24hr_vol={last_24_vol}"

    url = f"{url}&include_24hr_change={last_24_change}"

    url = f"{url}&include_last_updated_at={last_update_at}"

    url = url.lower()

    r = requests.get(url)

    response_dict = json.loads(r.content)

    if supply:
        for i in response_dict:
            response_dict[i]["circulating_supply"] = get_circulating_supply(i)
            response_dict[i]["total_supple"] = get_total_supply(i)
            response_dict[i]["max_supply"] = get_max_supply(i)

    return response_dict


def get_circulating_supply(coin):
    """
    Get the available circulating supply of a specific coin from CoinGecko website.

    Paramaters
    ----------
        coin (str): An available coin name from CoinGecko website.

    Return
    ------
        ammount (int): The circulating supply ammount.
    """
    url = f"https://www.coingecko.com/en/coins/{coin}"
    r = requests.get(url)
    html = BeautifulSoup(r.content, "html.parser")
    xpath_finder = etree.HTML(str(html))

    circtulating_supply = xpath_finder.xpath(
        "/html/body/div[5]/div[4] \
                    /div[1]/div/div[2]/div[2]/div[2]/div[1]/span[2]"
    )

    # Check if the list is empty
    if not circtulating_supply:
        circtulating_supply = xpath_finder.xpath(
            "/html/body/div[5]/div[5] \
                    /div[1]/div/div[2]/div[2]/div[2]/div[1]/span[2]"
        )

    if not circtulating_supply:
        return None

    circtulating_supply = circtulating_supply[0].text
    circtulating_supply = circtulating_supply.replace("\n", "").replace(",", "")

    if circtulating_supply == "∞":
        return None

    return int(circtulating_supply)


def get_total_supply(coin):
    """
    Get the total supply of a specific coin from CoinGecko website.

    Paramaters
    ----------
        coin (str): An available coin name from CoinGecko website.

    Return
    ------
        ammount (int): The circulating supply ammount.
    """
    url = f"https://www.coingecko.com/en/coins/{coin}"
    r = requests.get(url)
    html = BeautifulSoup(r.content, "html.parser")
    xpath_finder = etree.HTML(str(html))

    circtulating_supply = xpath_finder.xpath(
        "/html/body/div[5]/div[4] \
                    /div[1]/div/div[2]/div[2]/div[2]/div[2]/span[2]"
    )

    if not circtulating_supply:
        circtulating_supply = xpath_finder.xpath(
            "/html/body/div[5]/div[5] \
                    /div[1]/div/div[2]/div[2]/div[2]/div[2]/span[2]"
        )

    if not circtulating_supply:
        return None

    circtulating_supply = circtulating_supply[0].text
    circtulating_supply = circtulating_supply.replace("\n", "").replace(",", "")

    if circtulating_supply == "∞":
        return None

    return int(circtulating_supply)


def get_max_supply(coin):
    """
    Get the max supply of a specific coin from CoinGecko website.

    Paramaters
    ----------
        coin (str): An available coin name from CoinGecko website.

    Return
    ------
        ammount (int): The circulating supply ammount.
    """
    url = f"https://www.coingecko.com/en/coins/{coin}"
    r = requests.get(url)
    html = BeautifulSoup(r.content, "html.parser")
    xpath_finder = etree.HTML(str(html))  #

    circtulating_supply = xpath_finder.xpath(
        "/html/body/div[5]/div[4] \
                    /div[1]/div/div[2]/div[2]/div[2]/div[3]/span[2]"
    )

    if not circtulating_supply:
        circtulating_supply = xpath_finder.xpath(
            "/html/body/div[5]/div[5] \
                    /div[1]/div/div[2]/div[2]/div[2]/div[3]/span[2]"
        )

    if not circtulating_supply:
        return None

    circtulating_supply = circtulating_supply[0].text
    circtulating_supply = circtulating_supply.replace("\n", "").replace(",", "")

    if circtulating_supply == "∞":
        return None

    return int(circtulating_supply)
