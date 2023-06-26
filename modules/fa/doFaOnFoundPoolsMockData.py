import sys
sys.path.append('../..')
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

# Website links
tokensniffer_url = "https://tokensniffer.com/token/"
dextools_url = "https://www.dextools.io/app/en/"

pools = db.get_all_pools("pools_found")
for pool in pools:
    # if token1 and token2 are swapped
    if pool[8] == "WETH":
        newPool = list(pool)
        weth = newPool[8]
        token = newPool[10]
        newPool[8] = token
        newPool[10] = weth
        pool = tuple(newPool)

    # if eth
    if pool[1] == "ethereum" and pool[8] != "fUSDC-6e5e":

        # print(pool[8], tokensniffer_url, dextools_url,
        #       pool[7], pool[5], pool[2], pool[3], pool[1])
        # print(pool[7])
        result = full_fa(pool[8], tokensniffer_url, dextools_url,
                         pool[7], pool[5], pool[2], pool[3], pool[1])

        # if 3/3 -- add to new db
        if result > 1 and db.check_if_saved('pools_passed_fa', pool[_pool_address]) == False:
            # db.add_pool('pools_passed_fa', pool[1], pool[2], pool[3], pool[4],
            #                      pool[5], pool[6], pool[7], pool[8], pool[9], pool[10])
            db.copy_pool('pools_found', 'pools_passed_fa', pool[_pool_address])

            #example
            #db.edit_pool('pools_passed_fa', pool[_pool_address], 'passed_fa1', 1)
                         #name of table   , pool address       , column name , 1 for true

            print(pool[8] + " added to DB")
