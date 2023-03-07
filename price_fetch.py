from moralis import evm_api

from moralis_key import moralis_key

api_key = 
price_data = []

for to_block in range(16323500, 16323550, 10):
	params = {
		"address": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
		"chain": "eth",
		"to_block": to_block
	}
	result = evm_api.token.get_token_price(
		api_key=api_key,
		params=params,
		)

price_data.append(result)

print(price_data)
