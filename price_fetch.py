from moralis import evm_api

from moralis_key import moralis_key

api_key = moralis_key

price_data = []

#Mockdata with a random shitcoin that is new rn

for to_block in range(16776814, 16777061, 10):
	params = {
		"address": "0x474EB08D814C048D92c07Dc3D1d382254abfF08d",
		"chain": "eth",
		"to_block": to_block
	}
	result = evm_api.token.get_token_price(
		api_key=api_key,
		params=params,
	)
	price_data.append(result)

print(price_data)
