from web3 import Web3
from web3.middleware import geth_poa_middleware
import abi
from web3.contract import ContractEvent


w3 = Web3(Web3.HTTPProvider("http://larslund.in:8545"))
print(f"Connected: {w3.isConnected()}")


w3.middleware_onion.inject(geth_poa_middleware, layer=0)

token_address = '0x8505b9d2254a7ae468c0e9dd10ccea3a837aef5c' # Compound


from web3.contract import Contract
from web3.contract import ConciseContract

# contract = Contract(address=token_address, abi=abi.erc20)
token_contract = w3.eth.contract(address=token_address, abi=abi.erc20)
# token = ConciseContract(token_contract) 

# tx_receipt = w3.eth.getTransactionReceipt('0x36179c342e90bf119b4be11b95324b24d4926a83577d966db6ab2ad03a18dc7a')
# for log in tx_receipt.logs:
#     if log.address == token_address:# and log.topics[0] == token.events.Transfer().abi['topics'][0]:
#         print(log)
#         #transfer_event =  #token.events.Transfer().processLog(log)
#         break

# # from_address = transfer_event.args['_from']
# # to_address = transfer_event.args['_to']
# # amount = transfer_event.args['_value']

# # print("from_address",from_address)
# # print("to_address",to_address)
# # print("amount",amount)