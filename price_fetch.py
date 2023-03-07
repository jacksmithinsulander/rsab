from moralis import evm_api
import time
from moralis_key import moralis_key

api_key = moralis_key

price_data = []

unix_timestamp = str(time.time())

params_date = {
	"date": unix_timestamp, 
	"chain": "eth", 
}

current_block = evm_api.block.get_date_to_block(
	api_key=api_key,
	params=params_date,
)
#print(current_block['timestamp'])

#Mockdata with a random shitcoin that is new rn
for to_block in range(16776982, int(current_block['timestamp']), 10):
	params = {
		"address": "0x8e893280FABc738f539e479FD469E5eeBb710E91",
		"chain": "eth",
		"to_block": to_block
	}
	result = evm_api.token.get_token_price(
		api_key=api_key,
		params=params,
	)
	price_data.append(result)

#print(price_data)

price_arr = [obj["usdPrice"] for obj in price_data]

#fint bottom and top (only bottom PRIOR to top)
def btmtop_finder(prices):
	n = len(prices)
	highest = max(prices)
	highest_index = prices.index(highest)
	lowest = min(prices[:highest_index])
	print("The highest price is " + str(highest) + 
		" And the lowest price before that is " + str(lowest))
	fibretracement_finder(highest, lowest)

#function that calculates .786 retracement and .618 retracement
def fibretracement_finder(btm, top):
	x = top - btm
	_786 = top - (0.786 * x)
	_618 = top - (0.618 * x)
	print(_786, _618)

btmtop_finder(price_arr)
