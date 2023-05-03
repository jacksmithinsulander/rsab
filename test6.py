from web3 import Web3
import abi
import decimal

w3 = Web3(Web3.HTTPProvider("http://larslund.in:8545"))

pool_address = w3.toChecksumAddress("0x9b0Ff586031f4D64D72Cb624f20e62991dE5e27D")
pool_contract = w3.eth.contract(address=pool_address, abi=abi.pools['polygon']['uniswap3'])

def token_price():
    token0, token1 = pool_contract.functions.token0().call(),  pool_contract.functions.token1().call()
    print(f"Token 0 {token0}")
    print(f"Token 1 {token1}")

token_price()