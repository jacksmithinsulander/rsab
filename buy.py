from web3 import Web3
import abi
from dotenv import load_dotenv
import os
import json
from uniswap_universal_router_decoder import FunctionRecipient, RouterCodec
from eth_account import Account

load_dotenv()

acc = Account.from_key(os.getenv("PRIVATE_KEY"))
assert acc.address == Web3.to_checksum_address(os.getenv("WALLET_ADDRESS"))

#my_address = os.getenv("WALLET_ADDRESS")
infura_api = os.getenv("INFURA_API")

w3 = Web3(Web3.HTTPProvider(infura_api))
result = w3.isConnected()
print('Web3 is connected? ', result)

codec = RouterCodec() 

#Test token uniswap
#uni = 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984
#uni = '0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45'
uni = '0x4648a43B2C14Da09FdF82B161150d3F634f40491'
abi = json.loads('[{\"inputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"permit2\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"weth9\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"seaport\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"nftxZap\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"x2y2\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"foundation\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sudoswap\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"nft20Zap\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"cryptopunks\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"looksRare\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"routerRewardsDistributor\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"looksRareRewardsDistributor\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"looksRareToken\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"v2Factory\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"v3Factory\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"pairInitCodeHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"poolInitCodeHash\",\"type\":\"bytes32\"}],\"internalType\":\"struct RouterParameters\",\"name\":\"params\",\"type\":\"tuple\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"inputs\":[],\"name\":\"ContractLocked\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"ETHNotAccepted\",\"type\":\"error\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"commandIndex\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"message\",\"type\":\"bytes\"}],\"name\":\"ExecutionFailed\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"FromAddressIsNotOwner\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"InsufficientETH\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"InsufficientToken\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"InvalidBips\",\"type\":\"error\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"commandType\",\"type\":\"uint256\"}],\"name\":\"InvalidCommandType\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"InvalidOwnerERC1155\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"InvalidOwnerERC721\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"InvalidPath\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"InvalidReserves\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"LengthMismatch\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"NoSlice\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"SliceOutOfBounds\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"SliceOverflow\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"ToAddressOutOfBounds\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"ToAddressOverflow\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"ToUint24OutOfBounds\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"ToUint24Overflow\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"TransactionDeadlinePassed\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"UnableToClaim\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"UnsafeCast\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"V2InvalidPath\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"V2TooLittleReceived\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"V2TooMuchRequested\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"V3InvalidAmountOut\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"V3InvalidCaller\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"V3InvalidSwap\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"V3TooLittleReceived\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"V3TooMuchRequested\",\"type\":\"error\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"RewardsSent\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"bytes\",\"name\":\"looksRareClaim\",\"type\":\"bytes\"}],\"name\":\"collectRewards\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes\",\"name\":\"commands\",\"type\":\"bytes\"},{\"internalType\":\"bytes[]\",\"name\":\"inputs\",\"type\":\"bytes[]\"}],\"name\":\"execute\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes\",\"name\":\"commands\",\"type\":\"bytes\"},{\"internalType\":\"bytes[]\",\"name\":\"inputs\",\"type\":\"bytes[]\"},{\"internalType\":\"uint256\",\"name\":\"deadline\",\"type\":\"uint256\"}],\"name\":\"execute\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"uint256[]\",\"name\":\"\",\"type\":\"uint256[]\"},{\"internalType\":\"uint256[]\",\"name\":\"\",\"type\":\"uint256[]\"},{\"internalType\":\"bytes\",\"name\":\"\",\"type\":\"bytes\"}],\"name\":\"onERC1155BatchReceived\",\"outputs\":[{\"internalType\":\"bytes4\",\"name\":\"\",\"type\":\"bytes4\"}],\"stateMutability\":\"pure\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"\",\"type\":\"bytes\"}],\"name\":\"onERC1155Received\",\"outputs\":[{\"internalType\":\"bytes4\",\"name\":\"\",\"type\":\"bytes4\"}],\"stateMutability\":\"pure\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"\",\"type\":\"bytes\"}],\"name\":\"onERC721Received\",\"outputs\":[{\"internalType\":\"bytes4\",\"name\":\"\",\"type\":\"bytes4\"}],\"stateMutability\":\"pure\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes4\",\"name\":\"interfaceId\",\"type\":\"bytes4\"}],\"name\":\"supportsInterface\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"pure\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"int256\",\"name\":\"amount0Delta\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"amount1Delta\",\"type\":\"int256\"},{\"internalType\":\"bytes\",\"name\":\"data\",\"type\":\"bytes\"}],\"name\":\"uniswapV3SwapCallback\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"stateMutability\":\"payable\",\"type\":\"receive\"}]')

#Test token usd
contract_instance = w3.eth.contract(address=uni, abi=abi)
print(contract_instance.all_functions())
usdc = 0x07865c6E87B9F70255377e024ace6630C1Eaa37F
chain = "goerli"
dex = "uniswap"

weth_token_address = Web3.to_checksum_address("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6")
uni_token_address = Web3.to_checksum_address("0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984")

v2_path = [weth_token_address, uni_token_address]
v2_in_amount = int(0.001 * 10**18)
v2_out_amount = 0

encoded_data = (
	codec
	.encode
	.chain()
	.wrap_eth(FunctionRecipient.ROUTER, total_in_amount)
	.v2_swap_exact_in(FunctionRecipient.SENDER, v2_in_amount, v2_out_amount, v2_path, payer_is_sender=False)
	.build(codec.get_default_deadline())
);

tx_params = {
	"from": acc.address,
	"to": uni,
	"gas": 300_000,
	"maxPriorityFeePerGas": w3.eth.max_priority_fee,
	"maxFeePerGas": int(w3.eth.gas_price * 1.1),
	"type": '0x2',
	"chainId": w3.eth.chain_id,
	"value": total_in_amount,
	"nonce": w3.eth.get_transaction_count(acc.address),
	"data": encoded_data
}

e = w3.eth.estimate_gas(tx_params)
print(e)

raw_transaction = w3.eth.account.sign_transaction(tx_params, acc.key).rawTransaction
trx_hash = w3.eth.send_raw_transaction(raw_transaction)
print(trx_hash.hex())
