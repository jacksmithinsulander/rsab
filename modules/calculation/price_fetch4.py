from web3 import Web3
from abi import ERC20ABI, LPABI
import decimal
import json

web3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

token_address = web3.to_checksum_address(
	"0xD0afa798a59A4fDb7F833435ee92E89d339C8E49")
token_contract = web3.eth.contract(address=token_address, abi=ERC20ABI)

CONTRACT_CREATION_BLOCK = 17568898
events = token_contract.events.Transfer.get_logs(fromBlock=CONTRACT_CREATION_BLOCK)

for event in events:
	transaction_hash = web3.to_hex(event["transactionHash"])
	transaction = web3.eth.get_transaction(transaction_hash)
	print(transaction["value"])

#print(events)
