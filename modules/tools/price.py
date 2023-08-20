from web3 import Web3

#TEST DATA
token_address = "0xe4eFDd2eb216A4620cfA55c5cC67Bd09DC64Ff24"
lp_address = "0x1D9992600D22D336E9aB9F0807989FEb945aEDCe"
weth_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

erc20_abi = '[{"constant": true,"inputs": [],"name": "name","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "_spender","type": "address"},{"name": "_value","type": "uint256"}],"name": "approve","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "totalSupply","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "_from","type": "address"},{"name": "_to","type": "address"},{"name": "_value","type": "uint256"}],"name": "transferFrom","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "decimals","outputs": [{"name": "","type": "uint8"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [{"name": "_owner","type": "address"}],"name": "balanceOf","outputs": [{"name": "balance","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "symbol","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "_to","type": "address"},{"name": "_value","type": "uint256"}],"name": "transfer","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [{"name": "_owner","type": "address"},{"name": "_spender","type": "address"}],"name": "allowance","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"payable": true,"stateMutability": "payable","type": "fallback"},{"anonymous": false,"inputs": [{"indexed": true,"name": "owner","type": "address"},{"indexed": true,"name": "spender","type": "address"},{"indexed": false,"name": "value","type": "uint256"}],"name": "Approval","type": "event"},{"anonymous": false,"inputs": [{"indexed": true,"name": "from","type": "address"},{"indexed": true,"name": "to","type": "address"},{"indexed": false,"name": "value","type": "uint256"}],"name": "Transfer","type": "event"}]'

eth = "https://eth.llamarpc.com"
web3 = Web3(Web3.HTTPProvider(eth))
print(f"Is web3 connected? {web3.is_connected()}")

def get_price(token1, token2, lp, abi):
    token = web3.eth.contract(address=token1, abi=abi)
    reserve = web3.eth.contract(address=token2, abi=abi)
    token_float = token.functions.balanceOf(lp).call()
    token_decimals = token.functions.decimals().call()
    token_amount = token_float / 10 ** token_decimals
    reserve_float = reserve.functions.balanceOf(lp).call()
    reserve_decimals = reserve.functions.decimals().call()
    reserve_amount = reserve_float / 10 ** reserve_decimals
    price = reserve_amount / token_amount
    print(f"Token bal = {token_amount}")
    print(f"Reserve bal = {reserve_amount}")
    print(f"Token price = {format(price, '.20f')}")
    return format(price, ".20f"), token 
