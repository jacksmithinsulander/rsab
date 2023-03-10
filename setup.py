print("Hello you filthy, degenerate ape. Lets set up this shitcoinbot of yours")
print("=======================================================================")
print('First of what EVMs would you like to "trade"(read gamble) on? Answer with the coresponding capitalized letters, separated by commas')
chains = input("Ethereum mainnet (E), Arbitrum (A), Optimism (O), Polygon (P), Avalanche (V), Fantom (F), Binance smart chain (B)")
#print(chains)
#match chains: 
#	case "E":
#		print("You choose Ethereum main net")
#	case "A":
#		print("You choose Arbitrum")
#	case "O":
#		print("You choose Optimism")
#	case "P":
#		print("You choose Polygon")
#	case "V":
#		print("You choose Avalanche")
#	case "F":
#		print("You choose Fantom")
#	case "B":
#		print("You choose binance smart chain")
#	case other:
#		print("Input error, you messed up, try again")
#apparently the debian package didnt have python3.10, so righ tnow I have to use
#this outdated and totally AWFUL syntax
#the idea however is that i will iterate over this statement, and write it as 
#a function that builds up an object, and once that object is created
#the program will push it into a new file, which will act as the configuration 
#file, then everything else is taking in parameters from that program

chains_arr = chains.split(", ")
print(chains_arr)

#now that i see this its kind of stupid, figure out a way to write it cleaner
def chain_chooser(chainarr):
	for x in chainarr:
		if x == "E":
			print("You have chosen Ethereum mainnet.")
		elif x == "A":
			print("You have chosen Arbitrum.")
		elif x == "O":
			print("You have chosen Optimism.")
		elif x == "P":
			print("You have chosen Polygon.")
		elif x == "V":
			print("You have chosen Avalanche.")
		elif x == "F":
			print("You have chosen Fantom.")
		elif x == "B":
			print("You have chosen Binance Smart Chain.")
		else:
			print("Input error. Please try again.")

chain_chooser(chains_arr)