
import db.main as db
from fa import full_fa
_net = 1
_netShort = 2
_netExtra = 3
_poolMainContract = 4
_poolAddress = 5
_timeCreated = 6
_token1Address = 7
_token1Symbol = 8
_token2Address = 9
_token2Symbol = 10

# Website links
tokensniffer_url = "https://tokensniffer.com/token/"
dextools_url = "https://www.dextools.io/app/en/"

pools = db.getAllPools()
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
        if result == 1:
            db.addPoolToPassedFA(pool[1], pool[2], pool[3], pool[4],
                                 pool[5], pool[6], pool[7], pool[8], pool[9], pool[10])
            print(pool[8] + " added to DB")
