import os 
import sys
import json
import dotenv
from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account

with open('usdc_abi.json', 'r') as file:
    usdc_contract_abi = json.load(file)

with open('weth_abi.json', 'r') as file:
    weth_contract_abi = json.load(file)

sys.path.append("../..")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

config_file_path = os.path.join(grandparent_dir, 'conf.json')

with open(config_file_path, "r") as file:
    conf = json.load(file)

rebalancing = conf["rebalancing"]

#For testing purposes I will make the token use usdc and eth on the goerli test net

print(rebalancing)

load_dotenv()

acc = Account.from_key(os.getenv("PRIVATE_KEY"))

assert acc.address == Web3.to_checksum_address(os.getenv("WALLET_ADDRESS"))

print('Accoutn: ', acc.address)
#my_address = os.getenv("WALLET_ADDRESS")
infura_api = os.getenv("INFURA_API")

print(infura_api)

w3 = Web3(Web3.HTTPProvider(infura_api))
result = w3.is_connected()
print('Web3 is connected? ', result)

weth = Web3.to_checksum_address("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6")
usdc = Web3.to_checksum_address("0xe27658a36ca8a59fe5cc76a14bde34a51e587ab4")

usdc_instance = w3.eth.contract(address=usdc, abi=usdc_contract_abi)
weth_instance = w3.eth.contract(address=weth, abi=weth_contract_abi)

#weth_balance = weth.functions.balanceOf(acc.address).call()
usdc_balance = usdc_instance.functions.balanceOf(acc.address).call()
weth_balance = weth_instance.functions.balanceOf(acc.address).call()
#usdc_abi = Web3.eth.contract(address=usdc).abi

#print(contract_abi)
print(usdc_balance, weth_balance)
