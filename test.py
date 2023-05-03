from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
from time import sleep
import abi 
# connect to your node via RPC
w3 = Web3(Web3.HTTPProvider("http://larslund.in:8545"))
print(w3.isConnected())
#sleep(10)
# add POA middleware (if necessary)
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
#



block = w3.eth.getBlock(41445274)
print(block)


# define contract addresses and ABIs
pool_address = '0x2d4e28956e83c49Ac61DEe9B14ABF21B7374F7D2'
usdc_address = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
token_address = '0x8505b9d2254A7Ae468c0E9dd10Ccea3A837aef5c' # Compound
pool_abi = abi.pools['polygon']['uniswap3'] # insert the Uniswap liquidity pool ABI here
token_abi = abi.erc20  # insert the ERC20 token ABI here
print("set local variables")

# load contract instances
pool_contract = w3.eth.contract(address=pool_address, abi=pool_abi)
print(f"set pool contract {pool_contract}")
token_contract = w3.eth.contract(address=token_address, abi=token_abi)
print(f"set token contract {token_contract}")

# get the block number when the pool was created
print(pool_contract.events.Initialize.getLogs(fromBlock=41444673))
pool_creation_event = pool_contract.events.Initialize.getLogs(fromBlock=41444673)[0]
creation_block_number = pool_creation_event['blockNumber']

# iterate over all blocks since the pool creation
historical_price_in_usdcs = []
numbers = [41445274,41445428 ]
for block_number in numbers:# range(41445274 ,   41445428  ):#w3.eth.blockNumber + 1):
    print(f"checking {block_number}")
    block = w3.eth.getBlock(block_number)
    print(block)
    for tx_hash in block['transactions']:
        tx = w3.eth.getTransaction(tx_hash)
        try:
            # get the tokens bought and sold in the swap
            event = pool_contract.events.Swap.getLogs(transactionHash=tx_hash)[0]
            bought_amount, sold_amount = event['args']['amount1'], event['args']['amount0']
            #print(f"buy amount{bought_amount}")
            # get the current USDC price of the token
            usdc_reserve, token_reserve = pool_contract.functions.getReserves().call()
            current_price_in_usdcs = usdc_reserve / token_reserve

            # add the historical price to the list
            historical_price_in_usdcs.append((block.timestamp, current_price_in_usdcs))
        except Exception as e:
            print(e)
            pass

# sort the historical prices by timestamp
historical_price_in_usdcs.sort(key=lambda x: x[0])

# print the historical prices
for price in historical_price_in_usdcs:
    print(f"{price[0]}: {price[1]} USDC")