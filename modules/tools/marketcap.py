from modules.tools.price import get_price
from loguru import logger


def calculate_marketcap(token1, token2, lp, abi):
    price, token = get_price(token1, token2, lp, abi)
    total_supply = token.functions.totalSupply().call()
    marketcap = price * total_supply
    logger.debug(f"marketcap = {marketcap}")
    return marketcap
