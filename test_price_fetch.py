from modules.calculation.price_fetch import *
from loguru import logger
from modules.balancer.balancer_main import Balancer
import db.main as db
logger.debug("Imports done")

balancer = Balancer()

pool_list = db.get_all_pools('pools_found')
logger.debug(pool_list[8])
w3 = balancer.w3(pool_list[8][1])
block_number = w3.eth.block_number

price_fetch_v2(pool_list[8], block_number)

#price in usd for 1 Polygon
#0.000000000006549692684170795