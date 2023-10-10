import os
import sys
import json
import dotenv
from web3 import Web3
from loguru import logger
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

# For testing purposes I will make the token use usdc and eth on the goerli test net

logger.debug(rebalancing)

load_dotenv()

acc = Account.from_key(os.getenv("PRIVATE_KEY"))

assert acc.address == Web3.to_checksum_address(os.getenv("WALLET_ADDRESS"))

logger.debug('Accoutn: ', acc.address)
# my_address = os.getenv("WALLET_ADDRESS")
infura_api = os.getenv("INFURA_API")

logger.debug(infura_api)

w3 = Web3(Web3.HTTPProvider(infura_api))
result = w3.is_connected()
logger.debug('Web3 is connected? ', result)

weth = Web3.to_checksum_address("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6")
usdc = Web3.to_checksum_address("0xe27658a36ca8a59fe5cc76a14bde34a51e587ab4")

usdc_instance = w3.eth.contract(address=usdc, abi=usdc_contract_abi)
weth_instance = w3.eth.contract(address=weth, abi=weth_contract_abi)

# weth_balance = weth.functions.balanceOf(acc.address).call()
usdc_balance = usdc_instance.functions.balanceOf(acc.address).call()
weth_balance = weth_instance.functions.balanceOf(acc.address).call()
# usdc_abi = Web3.eth.contract(address=usdc).abi

# logger.debug(contract_abi)
logger.debug(usdc_balance, weth_balance)


def check_values(x, y):
    threshold_x = (x + y) * 0.4
    threshold_y = (x + y) * 0.6
    logger.debug("Now x and y are: ", x, y)
    logger.debug("And they should be: ", threshold_x, threshold_y)
    if x > threshold_x:
        logger.debug("now x is: ", x)
        excess_x = x - threshold_x
        x -= excess_x
        logger.debug("Adjusted x to threshold_x:", x)
    elif y > threshold_y:
        logger.debug("now y is", y)
        excess_y = y - threshold_y
        y -= excess_y
        logger.debug("Adjusted y to threshold_y:", y)


# Example usage
check_values(10, 5)
check_values(4, 10)
check_values(5, 5)
check_values(55555, 1)
check_values(420, 666)
