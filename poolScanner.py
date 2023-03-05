from time import sleep
from web3 import Web3
import db.main as db
from apiKey import apiKey

import abi

swapList = {
    'uniswap3' : '0x1F98431c8aD98523631AE4a59f267346ea31F984'
}

netList = ['mainnet']

while True:
    for net in netList:
        w3 = Web3(Web3.HTTPProvider(
            f"https://{net}.infura.io/v3/{apiKey}"))
        print(f"Connection to {net}: {w3.isConnected()}")
        for currentSwap in swapList:
            contract = w3.eth.contract(address=Web3.toChecksumAddress(
                swapList[currentSwap]), abi=abi.swap[currentSwap])
            
            latestPools = contract.events.PoolCreated.getLogs(
                fromBlock=w3.eth.block_number - 1000)
            
            for pool in latestPools:
                poolAddress = pool['args']['pool']
                if (db.checkIfSaved(poolAddress)):
                    print(f'Already saved {poolAddress}')
                else:
                    token1address = pool['args']['token0']
                    token1 = w3.eth.contract(token1address, abi=abi.erc20)
                    token1symbol = token1.functions.symbol().call()

                    token2address = pool['args']['token1']
                    token2 = w3.eth.contract(token2address, abi=abi.erc20)
                    token2symbol = token2.functions.symbol().call()

                    unixTime = w3.eth.getBlock(pool['blockNumber']).timestamp
                    db.addPool(net, "test", poolAddress, unixTime, token1address, token1symbol, token2address, token2symbol)
    print(f"Currently {db.countPools()} pools saved")
    print(f"Sleeping 30 seconds before next check")
    sleep(30)