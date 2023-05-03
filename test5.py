from web3 import Web3
import abi


w3 = Web3(Web3.HTTPProvider("http://larslund.in:8545"))
tx_hash = '0x05c1bc33c0e3e0be047272274e40336d6312e3dbbff145e39c09d0eb591c0382'
contract_address = "0x8505b9d2254a7ae468c0e9dd10ccea3a837aef5c"

def get_erc20_transfers(tx_hash):
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    tx = w3.eth.getTransaction(tx_hash)

    print('Amount: ', w3.fromWei(tx['value'], 'ether'))
    print('From: ', tx['from'])
    print('To: ', tx['to'])


    #contract_address = receipt['address']
    erc20_abi = abi.erc20
    cc = w3.toChecksumAddress(contract_address)
    erc20_contract = w3.eth.contract(address=cc, abi=erc20_abi)

    events = erc20_contract.events.Transfer().processReceipt(tx_receipt)

    # for event in events:
    #     print(event)
    return events



#t[0]['args']['value']

t = get_erc20_transfers(tx_hash)

