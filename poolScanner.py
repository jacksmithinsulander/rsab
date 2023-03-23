from datetime import datetime
from time import sleep
from web3 import Web3
import db.main as db
from swapList import swapList
from rpcList import rpcList
from web3.middleware import geth_poa_middleware

import abi

balancer = 0
lastBlocks = {
    'ethereum': 0,
    'polygon': 0,
    'arbitrum': 0
}

for net in rpcList:
    rpc_link = rpcList[net]['links'][0]
    w3 = Web3(Web3.HTTPProvider(rpc_link))
    lastBlocks[net] = w3.eth.block_number - 50


while True:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"# {now} ######################################")
    for net in rpcList:
        rpc_link = rpcList[net]['links'][balancer % len(rpcList[net]['links'])]
        w3 = Web3(Web3.HTTPProvider(rpc_link))
        if (net == 'polygon'):
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        currentBlock = w3.eth.block_number
        # fromBlock = lastBlock - 50
        print(f"  # Checking {net} # Blocks {lastBlocks[net]}-{currentBlock}")
        print(f"  # Using {rpc_link}")
        #print(f"Connection to {net}: {w3.isConnected()}")
        for swap in swapList[net]:
            print(
                f"    # Checking for pools by {swap}")
            contract = w3.eth.contract(address=Web3.toChecksumAddress(
                swapList[net][swap]['address']), abi=abi.swaps[net][swap])

            exec(
                f"getPool = contract.events.{swapList[net][swap]['eventName']}.getLogs")
            latestPools = getPool(fromBlock=lastBlocks[net])

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
                    db.addPool(net, rpcList[net]['short'], rpcList[net]['extra'], swapList[net][swap]['address'], poolAddress, unixTime,
                               token1address, token1symbol, token2address, token2symbol)
        lastBlocks[net] = currentBlock
    print(f"Currently {db.countPools()} pools saved")
    print(f"Sleeping 30 seconds before next check")
    sleep(30)
    print("###########################################")
    balancer += 1
