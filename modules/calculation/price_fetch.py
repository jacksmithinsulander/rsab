from web3 import Web3
from modules.calculation.abi import ERC20ABI, LPABI
from modules.balancer.balancer_main import Balancer
import decimal
from loguru import logger

balancer = Balancer()

_net = 1
_net_short = 2
_net_extra = 3
_pool_main_contract = 4
_pool_address = 5
_time_created = 6
_token1_address = 7
_token1_symbol = 8
_token2_address = 9
_token2_symbol = 10
_dex = 11
_creation_block = 12

#web3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

#print(web3.is_connected())

#lpAddress = web3.to_checksum_address("0x43A73Aaed6Aed1b1F5a693d77dD18C3121f24CAC")
#lpAddress = web3.to_checksum_address(input("Enter LP address: "))
#lpContract = web3.eth.contract(address=lpAddress, abi=LPABI)

# def __init__(self):

def uni_v2_price(web3, block_num, token0, token1, pool, net, dex):
	#token0, token1 = lpContract.functions.token0().call(), lpContract.functions.token1().call()
	lp_contract = web3.eth.contract(address = pool, abi=LPABI)
	reserves = lp_contract.functions.getReserves().call(block_identifier=block_num)
	print(f"{reserves} RESERVADOS")
	print(token0, token1)
	tkc0 = web3.eth.contract(address=token0, abi=ERC20ABI)
	tkc1 = web3.eth.contract(address=token1, abi=ERC20ABI)
	decimal0 = tkc0.functions.decimals().call()
	decimal1 = tkc1.functions.decimals().call()
	print(decimal0, decimal1)
	reserve0 = float(reserves[0] / 10 **decimal0)
	reserve1 = float(reserves[1] / 10 **decimal1)
	price = reserve1 / reserve0
	print("Reserve 0 = ", reserve0)
	print("Reserve 1 = ", reserve1)
	form_price = "{:.10f}".format(price)
	print(form_price)

#token_price()

def price_fetch(web3, creation_block, token0, token1, pool, net, dex):
	#creation_block = 17257452 #Lets find a more elegant way to do this later, maybe if this information is saved in our database?
	latest_block = web3.eth.block_number
	print(creation_block, latest_block)
	for block in range(creation_block, latest_block + 1):
		uni_v2_price(web3, block, token0, token1, pool, net, dex)

def price_fetch_v2(lp, block_num):
	w3 = balancer.w3(lp[_net])
	logger.debug(f"w3.is_connected() {w3.is_connected()}")
	lp_contract = w3.eth.contract(address=lp[_pool_address], abi=LPABI)
	logger.debug(f"lp_contract:{lp_contract}")
	reserves = lp_contract.functions.getReserves().call(block_identifier=block_num)
	logger.debug(f"reserves: {reserves}")
	w3 = balancer.w3(lp[_net])
	token0_contract = w3.eth.contract(address=lp[_token1_address], abi=ERC20ABI)
	decimal0 = token0_contract.functions.decimals().call()
	logger.debug(f"decimal0: {decimal0}")
	token1_contract = w3.eth.contract(address=lp[_token2_address], abi=ERC20ABI)
	decimal1 = token1_contract.functions.decimals().call()
	logger.debug(f"decimal1: {decimal1}")
	
	reserve0 = float(reserves[0] / 10 **decimal0)
	reserve1 = float(reserves[1] / 10 **decimal1)

#":.8f" fixes the print out to not use scientific notation
	logger.debug(f"reserve0: {reserve0:.8f}") 
	logger.debug(f"reserve1: {reserve1:.8f}")

	price = reserve0 / reserve1
	form_price = "{:.10f}".format(price)
	logger.debug(f"Price is: {form_price}")
