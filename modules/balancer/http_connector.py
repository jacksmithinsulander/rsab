import requests
from loguru import logger
url = "http://ip-api.com/json/"


def get_tor_session():
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050',
    }

    adapter = requests.adapters.HTTPAdapter(
        pool_connections=20, pool_maxsize=20)

    session.mount('http://', adapter)
    session.mount('https://', adapter)

    response = session.get(url)
    logger.debug(response.text)

    return session
