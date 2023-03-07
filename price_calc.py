#mockdata
price_arr = [10.5, 12.7, 9.8, 15.3, 16.1, 13.2, 11.9, 10.8, 9.5, 12.4]

#fint bottom and top (only bottom PRIOR to top)
def btmtop_finder(prices):
	n = len(prices)
	highest = max(prices)
	highest_index = prices.index(highest)
	lowest = min(prices[:highest_index])
	print("The highest price is " + str(highest) + 
		" And the lowest price before that is " + str(lowest))
	fibretracement_finder(highest, lowest)

def fibretracement_finder(btm, top):
	x = top - btm
	_786 = top - (0.786 * x)
	_618 = top - (0.618 * x)
	print(_786, _618)

btmtop_finder(price_arr)
