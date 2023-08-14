from loguru import logger
price_arr = [obj["usdPrice"] for obj in price_data]

#fint bottom and top (only bottom PRIOR to top)
def btmtop_finder(prices):
	n = len(prices)
	highest = max(prices)
	highest_index = prices.index(highest)
	lowest = min(prices[:highest_index])
	logger.debug("The highest price is " + str(highest) + 
		" And the lowest price before that is " + str(lowest))
	fibretracement_finder(highest, lowest)

#function that calculates .786 retracement and .618 retracement
def fibretracement_finder(btm, top):
	x = top - btm
	_786 = top - (0.786 * x)
	_618 = top - (0.618 * x)
	logger.debug(_786, _618)

btmtop_finder(price_arr)