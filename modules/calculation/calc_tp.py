from random import randint

mock_price = randint(100, 999)/100.00
#mock_price = 7

print("The mock price is " + str(mock_price))

def generate_tps(buyin_price):
	for i in range (10):
		print(2 ** (i + 1) * buyin_price)

generate_tps(mock_price)
