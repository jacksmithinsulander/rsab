from web3 import Web3
import abi

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/f69d94ced2f84d9d80b56b82c1b4e181'))
result = w3.isConnected()
print('Web3 is connected? ', result)

#def trade_exec(token_a, token_b, chain, dex)
