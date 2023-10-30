import db.main as db
from modules.onchain.rpc_list import rpc_list
from modules.tools.price import get_price
from web3_balancer import Web3_balancer
from loguru import logger

tor_toggle_placeholder = True

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


def iterate():
    pools = db.get_all_pools("pools_passed_fa")
    w3 = Web3_balancer(rpc_list, tor=tor_toggle_placeholder)
    # logger.debug(pools)
    for pool in pools:
        w3.net = pool[_net]
        # price_fetch()
        logger.debug(pool)
        result = get_price(
            w3, pool[12], pool[9], pool[7], pool[5], pool[1], pool[1])
