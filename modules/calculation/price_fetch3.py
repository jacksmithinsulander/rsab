from web3 import Web3
from abi import ERC20ABI, LPABI
import decimal

web3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

print(web3.is_connected())

lpAddress = web3.to_checksum_address("0x43A73Aaed6Aed1b1F5a693d77dD18C3121f24CAC")
lpContract = web3.eth.contract(address=lpAddress, abi=LPABI)
def uni_v2_price(block_num):
	token0, token1 = lpContract.functions.token0().call(), lpContract.functions.token1().call()
	reserves = lpContract.functions.getReserves().call(block_identifier=block_num)
	print(reserves)
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

def price_fetch():
	creation_block = 17257452 #Lets find a more elegant way to do this later, maybe if this information is saved in our database?
	latest_block = web3.eth.block_number
	print(creation_block, latest_block)
	for block in range(creation_block, latest_block + 1):
		uni_v2_price(block)

price_fetch()