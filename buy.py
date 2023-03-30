from web3 import Web3
import abi
from dotenv import load_dotenv
import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider(''))
result = w3.isConnected()
print('Web3 is connected? ', result)

#def trade_exec(token_a, token_b, chain, dex)
