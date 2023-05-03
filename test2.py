from web3 import Web3
from web3.middleware import geth_poa_middleware
import abi
from web3.contract import ContractEvent


w3 = Web3(Web3.HTTPProvider("http://larslund.in:8545"))
print(f"Connected: {w3.isConnected()}")

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

current_block = w3.eth.block_number

pool_address = '0x2d4e28956e83c49Ac61DEe9B14ABF21B7374F7D2'
usdc_address = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
token_address = '0x8505b9d2254A7Ae468c0E9dd10Ccea3A837aef5c' # Compound
pool_abi = abi.pools['polygon']['uniswap3'] # insert the Uniswap liquidity pool ABI here
token_abi = abi.erc20  # insert the ERC20 token ABI here
print("set local variables")


pool_contract = w3.eth.contract(address=pool_address, abi=pool_abi)
token_contract = w3.eth.contract(address=token_address, abi=token_abi)

start_block = 41444673

#tx_hash = pool_contract.web3.eth.getTransactionReceipt(pool_contract.constructor.buildTransaction()["transactionHash"]).transactionHash


historical_price_in_usdcs = []
# swap_event_signature = Web3.sha3(text='Swap(uint256,uint256,int256,int256,address)')
# SwapEvent = ContractEvent.factory(pool_abi, name='Swap', signature=swap_event_signature)
# swap_events = pool_contract.events.Swap.createFilter(fromBlock=start_block, toBlock=current_block).get_all_entries()



# Define the contract instances
pool_contract = w3.eth.contract(address=pool_address, abi=pool_abi)
token0_contract = w3.eth.contract(address=pool_contract.functions.token0().call(), abi=abi.erc20)
token1_contract = w3.eth.contract(address=pool_contract.functions.token1().call(), abi=abi.erc20)

token0_balance = token0_contract.functions.balanceOf(pool_address).call()
token1_balance = token1_contract.functions.balanceOf(pool_address).call()

print(f"Token 0 Balance: {token0_balance}")
print(f"Token 1 Balance: {token1_balance}")

token0decimal = 10e6
token1decimal = 10e18

balance = (token0_balance / token1_balance) 
print(f"Balance: {balance}")
price = balance * token1decimal / token0decimal
print(f"Current price: {price}")
#price2 = token1_balance / token0_balance
#print(f"Current price: {price2}")


#functionEvents = pool_contract.events.Swap.getLogs(fromBlock=start_block, toBlock=current_block)

for event in []: #functionEvents:
    block_number = event['blockNumber']
    print(f"Checking {block_number}")
    block = w3.eth.getBlock(block_number)
    # bought_amount, sold_amount = event['args']['amount1'], event['args']['amount0']
    # print(f"Bought: {bought_amount}")
    # print(f"Sold  : {sold_amount}")
    usdc_reserve, token_reserve = pool_contract.functions.getReserves().call()
    current_price_in_usdcs = usdc_reserve / token_reserve
    historical_price_in_usdcs.append((block.timestamp, current_price_in_usdcs))
    print(historical_price_in_usdcs)