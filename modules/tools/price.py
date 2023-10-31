from web3 import Web3
from loguru import logger
from modules.onchain import abi

_net = 1
_net_short = 2
_net_extra = 3
_pool_main_contract = 4
_pool_address = 5
_time_created = 6
_token1_address = 7
_token1_symbol = 8
_token2_address = 9
_token2_symbol = 10
_dex = 11
_creation_block = 12

# TEST DATA
# token_address = "0xe4eFDd2eb216A4620cfA55c5cC67Bd09DC64Ff24"
# lp_address = "0x1D9992600D22D336E9aB9F0807989FEb945aEDCe"
# weth_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

# eth = "https://eth.llamarpc.com"
# web3 = Web3(Web3.HTTPProvider(eth))
# logger.debug(f"Is web3 connected? {web3.is_connected()}")


def get_price(w3, lp):
    token = w3.eth.contract(address=lp[_token1_address], abi=abi.erc20)
    reserve = w3.eth.contract(address=lp[_token2_address], abi=abi.erc20)
    token_float = token.functions.balanceOf(lp[_pool_address]).call()
    token_decimals = token.functions.decimals().call()
    token_amount = token_float / 10 ** token_decimals
    reserve_float = reserve.functions.balanceOf(lp[_pool_address]).call()
    reserve_decimals = reserve.functions.decimals().call()
    reserve_amount = reserve_float / 10 ** reserve_decimals
    price = reserve_amount / token_amount
    logger.debug(f"Token bal = {token_amount}")
    logger.debug(f"Reserve bal = {reserve_amount}")
    logger.debug(f"Token price = {format(price, '.20f')}")
    return format(price, ".20f"), token
