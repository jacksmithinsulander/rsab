
import db.main as db

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

pools = db.getAllPools()
for pool in pools:

    # if eth

    # fullFa(pool[_token1Symbol],pool[2]...)
    # full_fa(token_name, tokensniffer_url, dextools_url, token_address,
    #    token_lp_pair, token_chain_short, token_chain_extra, token_chain)

    # if 3/3 -- add to new db

    print(pool)
