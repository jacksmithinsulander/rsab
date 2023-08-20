from modules.tools.price import get_price

def calculate_marketcap(token1, token2, lp, abi):
    price, token = get_price(token1, token2, lp, abi)
    total_supply = token.functions.totalSupply().call()
    marketcap = price * total_supply
    print(marketcap)
    return marketcap