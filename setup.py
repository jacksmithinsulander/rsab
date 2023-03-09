print("Hello you filthy, degenerate ape. Lets set up this shitcoinbot of yours")
print("=======================================================================")
print('First of what EVMs would you like to "trade"(read gamble) on? Answer with the coresponding capitalized letters, separated by commas')
chains = input("Ethereum mainnet (E), Arbitrum (A), Optimism (O), Polygon (P), Avalanche (V), Fantom (F), Binance smart chain (B)")
#print(chains)
match chains: 
	case "E":
		print("You choose Ethereum main net")
	case "A":
		print("You choose Arbitrum")
	case "O":
		print("You choose Optimism")
	case "P":
		print("You choose Polygon")
	case "V":
		print("You choose Avalanche")
	case "F":
		print("You choose Fantom")
	case "B":
		print("You choose binance smart chain")
	case other:
		print("Input error, you messed up, try again")
