import db.main as db
from modules.tools.price import get_price
from modules.balancer.balancer_main import Balancer
from loguru import logger

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
    balancer = Balancer()
    # logger.debug(pools)
    for pool in pools:
        w3 = balancer.w3(pool[_net])
        # price_fetch()
        logger.debug(pool)
        result = get_price(
            w3, pool[12], pool[9], pool[7], pool[5], pool[1], pool[1])
