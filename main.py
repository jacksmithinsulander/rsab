import datetime
import time
import web3
from web3 import Web3, EthereumTesterProvider
import json

from apiKey import apiKey

with open("./uniswap3abi.json") as f:
    info_json = json.load(f)
uniswap3abi = info_json["result"]


w3 = Web3(Web3.HTTPProvider(
    f"https://mainnet.infura.io/v3/{apiKey}"))
print(f"Connection to Ethereum: {w3.isConnected()}")

# w3.eth.get_block('latest')
# w3.eth.get_balance("")

# random shitcoin contract address
#   0x05C150ee0661967D34Eb4780C20fF3B259fF6813
#contract = w3.eth.contract("0x05C150ee0661967D34Eb4780C20fF3B259fF6813")

# uniswap v3 contract
uniswap3 = 0x1F98431c8aD98523631AE4a59f267346ea31F984
# has events for PoolCreated

# Standard abi for erc20 tokens I think
tokenAbi = [{"inputs": [], "name":"name", "outputs":[{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {
    "inputs": [], "name":"symbol", "outputs":[{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}]

contract = w3.eth.contract(address=Web3.toChecksumAddress(
    uniswap3), abi=uniswap3abi)
#events = contract.events.Transfer.getLogs(fromBlock=CONTRACT_CREATION_BLOCK)
PoolCreatedLast1000Blocks = contract.events.PoolCreated.getLogs(
    fromBlock=w3.eth.block_number - 5000)

def json_mkr(pool_addr, token_1, token_2, time_created):
	token_info = '{"poolAddr": "' + pool_addr + '", "token1": "' + token_1 + '", "token2": "' +  token_2 + '", "timeCreated": "' +  str(time_created) + '"}'
	token_json = json.loads(token_info)
	print(json.dumps(token_json, indent=4))
	with open("datascraped.json", "a") as file:
		json.dump(token_json, file, indent=4)

for pool in PoolCreatedLast1000Blocks:
    print("============================================")
    pool_name = pool['args']['pool']
    #print(f"Found Pool {pool['args']['pool']}")
    #print(f"Found Pool {pool_name}")
    token1 = w3.eth.contract(pool['args']['token0'], abi=tokenAbi)
    token1name = token1.functions.name().call()
    token1symbol = token1.functions.symbol().call()
    #print(f"Token 1: {token1name} ({token1symbol})")
    token2 = w3.eth.contract(pool['args']['token1'], abi=tokenAbi)
    token2name = token2.functions.name().call()
    token2symbol = token2.functions.symbol().call()
    #print(f"Token 2: {token2name} ({token2symbol})")
    unixTime = w3.eth.getBlock(pool['blockNumber']).timestamp
    dateTime = datetime.datetime.utcfromtimestamp(
        unixTime).strftime('%Y-%m-%d %H:%M:%S')
    #print(f"Created: {dateTime} {unixTime}")
    json_mkr(pool_name, token1symbol, token2symbol, unixTime)