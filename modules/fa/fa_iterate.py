import sys
import db.main as db
from modules.fa.fa import full_fa

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


accepted_pairing_tokens = [
	"WETH", "USDT", "USDC", "WBNB", "BUSD", "WMATIC", "WPLS", "DAI"
]

def pair_token_finder(token):
	if token in accepted_pairing_tokens:
		return True
	else:
		return False

def iterate():
	pools = db.get_all_pools("pools_found")
	print(pools)
	for pool in pools:		
		if (pair_token_finder(pool[8])):
			newPool = list(pool)
			weth = newPool[8]
			token = newPool[10]
			newPool[8] = token
			newPool[10] = weth
			pool = tuple(newPool)

		elif (pair_token_finder(pool[10])):
			newPool = list(pool)
			weth = newPool[10]
			token = newPool[8]
			newPool[8] = token
			newPool[10] = weth
			pool = tuple(newPool)

		if pool[8] != "fUSDC-6e5e":
			result = full_fa(
				pool[8], pool[7], pool[5], pool[2], pool[3], pool[1])
			if result > 1 and db.check_if_saved(
				'pools_passed_fa', pool[_pool_address]) == False:
				db.copy_pool(
					'pools_found', 'pools_passed_fa', pool[_pool_address])
				print(pool[8] + " added to DB")
