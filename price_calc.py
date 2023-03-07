prices = [10.5, 12.7, 9.8, 15.3, 16.1, 13.2, 11.9, 10.8, 9.5, 12.4]

n = len(prices)

highest = max(prices)

highest_index = prices.index(highest)
lowest = min(prices[:highest_index])

print("The highest price is " + str(highest) + 
	" And the lowest price before that is " + str(lowest))
