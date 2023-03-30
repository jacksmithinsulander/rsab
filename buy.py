from web3 import Web3
import abi
from dotenv import load_dotenv
import os

load_dotenv()

my_address = os.getenv("WALLET_ADDRESS")
infura_api = os.getenv("INFURA_API")

w3 = Web3(Web3.HTTPProvider(infura_api))
result = w3.isConnected()
print('Web3 is connected? ', result)

#Test token uniswap
uni = 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984
#Test token usd
usdc = 0x07865c6E87B9F70255377e024ace6630C1Eaa37F
chain = "goerli"
dex = "uniswap"

#def trade_exec(token_a, token_b, chain, dex)
