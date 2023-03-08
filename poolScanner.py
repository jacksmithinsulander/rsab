from datetime import datetime
from time import sleep
from web3 import Web3
import db.main as db
from swapList import swapList
from rpcList import rpcList

import abi


while True:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"# {now} ######################################")
    for net in rpcList:
        w3 = Web3(Web3.HTTPProvider(rpcList[net]['link']))
        lastBlock = w3.eth.block_number
        fromBlock = lastBlock - 5000
        print(f"  # Checking {net} # Blocks {fromBlock}-{lastBlock}")
        #print(f"Connection to {net}: {w3.isConnected()}")
        for swap in swapList[net]:
            print(
                f"    # Checking for pools by {swap}")
            contract = w3.eth.contract(address=Web3.toChecksumAddress(
                swapList[net][swap]['address']), abi=abi.swaps[swap])

            exec(
                f"getPool = contract.events.{swapList[net][swap]['eventName']}.getLogs")
            latestPools = getPool(fromBlock=fromBlock)

            for pool in latestPools:
                poolAddress = pool['args'][swapList[net][swap]
                                           ['poolAddress']]
                if (db.checkIfSaved(poolAddress)):
                    print(f'      Already saved {poolAddress}')
                else:
                    token1address = pool['args']['token0']
                    token1 = w3.eth.contract(token1address, abi=abi.erc20)
                    token1symbol = token1.functions.symbol().call()

                    token2address = pool['args']['token1']
                    token2 = w3.eth.contract(token2address, abi=abi.erc20)
                    token2symbol = token2.functions.symbol().call()

                    unixTime = w3.eth.getBlock(pool['blockNumber']).timestamp
                    db.addPool(net, "test", poolAddress, unixTime,
                               token1address, token1symbol, token2address, token2symbol)
    print(f"Currently {db.countPools()} pools saved")
    print(f"Sleeping 30 seconds before next check")
    sleep(30)
    print("###########################################")
