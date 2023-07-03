import db.main as db
from modules.calculation.price_fetch import price_fetch
from modules.balancer.balancer_main import Balancer

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
	#print(pools)
	for pool in pools:
		w3 = balancer.w3(pool[_net])
		#price_fetch()
		print(pool)
		result = price_fetch(
			w3, pool[12], pool[10], pool[9], pool[5], pool[1], pool[1])

