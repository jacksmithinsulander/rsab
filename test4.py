from web3 import Web3
import abi

# Connect to the Ethereum network using Infura node
w3 = Web3(Web3.HTTPProvider("http://larslund.in:8545"))

# Get the transaction hash you want to check
#tx_hash = '0x36179c342e90bf119b4be11b95324b24d4926a83577d966db6ab2ad03a18dc7a'

tx_hash = '0x05c1bc33c0e3e0be047272274e40336d6312e3dbbff145e39c09d0eb591c0382' #purchased COMP with USDC

# Get the transaction receipt
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

# Get the transaction details
tx = w3.eth.getTransaction(tx_hash)
print("tx",tx)

# Print the transaction details
print('Amount: ', w3.fromWei(tx['value'], 'ether'))
print('From: ', tx['from'])
print('To: ', tx['to'])

erc = ""
rec = ""

# Loop over receipts to extract ERC20 events
for receipt in tx_receipt['logs']:
    rec = receipt
    print("=============================")
    print(f"New receipt")
    print("=============================")
    print(receipt)
    print("=============================")
    # Get the contract address
    contract_address = receipt['address']

    # check if token is ERC20
    if w3.eth.getCode(contract_address) == b'':
        print("contract address was empty")
        continue
        
    # Get ERC20 ABI
    erc20_abi = abi.erc20

    # Load ERC20 contract
    erc20_contract = w3.eth.contract(address=contract_address, abi=erc20_abi)
    print("erc20_contract",erc20_contract)
    erc = erc20_contract

    # Decode ERC20 events
    
    # try:
    event = erc20_contract.events.Transfer().processReceipt(receipt)
    # except Exception as e:
    #     print("something was not decoded")
    #     print(e)
    #     continue

    # Extract transfer information
    transfer_from = event[0]['args']['from']
    transfer_to = event[0]['args']['to']
    transfer_value = event[0]['args']['value']

    # Print transfer information
    print(f'Transfer {transfer_value} Tokens from {transfer_from} to {transfer_to}')