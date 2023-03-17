"""
Planing flow
1. Function for checking if config file already exisist
	if exisist:
		redo it
	else
		cancel setup

	else do it #same path as redoing it
2. Program thats sets everything up
	2.1. Choose chains #will have to do it even if sticking with defaul config later on
	2.2. Choose if sticking with default options or custom ones
	if default, send it into the config file and end the setup
	else:
		2.2.1. Choose if changing all or just some of the settings
		2.2.2. Start a function that just calls the other functions to set each configuration. IF just changing some settings this master function skips the ones not selected
			2.2.2.1. Set profit taking size
			2.2.2.2. Set profit taking levels
			2.2.2.3. Set on / off rebalancing
			2.2.2.4. Set buy sizes
			2.2.2.5. Set stoploss rules
			2.2.2.6. FA on or off
				2.2.2.6.1. Finetune points thresholds
					2.2.2.6.1.1. Tokensniffer
					2.2.2.6.1.2. Dextools
					2.2.2.6.1.3. Dexscreener
				2.2.2.6.2. Finetune pass thresholds
3. Pass selection into a new config file
"""
print("Hello you filthy, degenerate ape. Lets set up this shitcoinbot of yours")
print("=======================================================================")
print('First of what EVMs would you like to "trade"(read gamble) on? Answer with the coresponding capitalized letters, separated by commas')
chains = input("Ethereum mainnet (E), Arbitrum (A), Optimism (O), Polygon (P), Avalanche (V), Fantom (F), Binance smart chain (B)\n")
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
			print("Input error. Please try again.\n")
chain_chooser(chains_arr)

print("=======================================================================")
print("Ait, now for the trading bot parameters, such as stop loss and profit taking")
param_choose = input("Do you want the standard (1) or custom (2) settings? Show standard settings (3)\n")

def param_choose_results(choice):
	if choice == "1":
		print("You selected the standard settings. wagmi")
	elif choice == "2":
		print("You want to be adventurous and tinker with you own settings")
	elif choice == "3":
		print("=======================================================================")
		print('The standard settings are inspired by the "little old lady" trading strategy.')
		print("The idea is that it basically takes profit each time that the value you hold is double to the value you initially bought")
		print('Just google (or use a better search engine like searx / gigablast / yandex) for the "little old lady" strategy to get a better idea of how it works')
		print('You are free to change booth the amount of profit taking and the actual levels of profit taking')
		print('Other than that, standard is also that the bot will rebalance your Eth / stables so that you hold "dry powder" for booth kinds of pairs')
		print('You can turn the rebalancing off')
		print('The bot will buy for 1% of the combined worth of eth / stables that your wallet has for each entry')
		print('You can change this to a static number if you like')
		print('Also, standard is to have a tiling stop loss att the 200 MA (read on the 4h chart)')
		print("This means that it will take this means that for the first (200 * 4h = 800 h = 33.33 days) you're without a stoploss")
		print('You can either choose to change this to a static stoploss, or a timebased one or a combination of stoplosses')
		print('Our "sophisticated" FA, is just that we check the token on dextools ratings, dexscreener ratings and tokensniffer')
		print('Our standard settings are that it has to reach a certain amount of "points" to "pass" each step')
		print('And in order to be a valid entry, a token must fullfill at least 2/3 passes')
		print('You can booth choose to finetune the points threshold, as well as the pass threshold')
		print('Or (NOT RECOMENDED) decide to remove the FA completly')
		print('However that would be stupid, because the fa is mostly checking the token on a contract level')
		print('Checking things like if it is possible to sell the token, if the liquidity is locked etc.')
	else:
		print("Didnt understand your input, try again\n")

param_choose_results(param_choose)

print("=======================================================================")
change_selection = input("Do you want to change all of these parameters (A) or only some (B) of them?\n")

#thinking through it all now and realising that this will need a massive rewrite
#at a later time, with a LOT of return functions
def profit_taking_config():
	print("=======================================================================")
	profit_taking = input('How many % profits do you want to take on each target levels? Answer with numbers ended by % sign, i.e. "50 %" or "100 %"(if you want to sell it all on first target)\n')
	if (profit_taking[:-2].isdigit() and 
		int(profit_taking.removesuffix(" %")) <= 100):
		print("Yes!")
	else:
		print("Something went wrong, retry")

def profit_target_config();
	print("=======================================================================")
	tp = input('Standard profit taking is each time the worth of what you hold is worth double of what you initially bought. So if you bought for $10, the bot will take profit each time the bag is worth $20. How many % gains would you prefer for each profit taking? answer with numbers ended by % sign.')
	if tp[:-2].isdigit():
		print("Perfect!")
	else:
		print("Something went wrong, retry")

def rebalancing_config();
	print("=======================================================================")
	want_rebalancing = input('Do you want autorebalancing? (Y / N)'):
	if want_rebalancing == "Y":
		print("Rebalancing is ON")
	elif want_rebalancing == "N":
		print("Rebalancing is OFF")

def bag_sizing():
	print("=======================================================================")
	dynamic_or_static = input("For bagsizing, would you like each bag to be (A) a dynamic %age of the ammount of dry powder your wallet holds or (B) a static number? Examples: Every time buy for 1 % of the dry powder or everytime buy for 1 dollar no matter what")
	if dynamic_or_static == "A":
		dynamic_size = input("You chose dynamic bag sizing. How many percentages should each buy be?")
	elif dynamic_or_static == "B":
		static_size = input("You chose static bag sizing. How many biden bucks would you like to gamble for each trade?")

def fa_on():
	print("=======================================================================")
	fa_toggle = input("FA (A) on or (B) off? (NOT RECOMENDED TO TURN OFF SINCE ITS ONLY CHECKING WETHER OR NOT YOU CAN ACTUALLY SELL THE SHITCOINS)")
	if fa_toggle == "A":
		print("FA is turned on")
	elif fa_toggle == "B":
		print("FA is turned off")

def fa_passes_settings():
	print("=======================================================================")
	fa_passes = input("The standard amount of passes for the 3 FA parameters are 2/3. Would you like to make it (A) 1/3, (B) 3/3 or (C) leave it as is?")
	if fa_passes == "A":
		print("1/3")
	elif fa_passes == "B":
		print("3/3")
	elif fa_passes == "C":
		print("2/3")

def stoploss_management():
	print("=======================================================================")
	stoploss_settings = input("The alternatives for potential stoplosses are (A) stoploss on the 200MA on the 4hr chart, (B) a static stoploss, (C) a timebased stoploss, (D) all of them, (E) some of them or (F) none of them.")
	if stoploss_settings == "A":
		print("You selected 200MA stoploss")
	elif stoploss_settings == "B":
		print("You selected a static stoploss")
	elif stoploss_settings == "C":
		print("You selected a timebased stoploss")
	elif stoploss_settings == "D":
		print("You selected all of the options.")
		#will need more configuring
	elif stoploss_settings  == "E":
		print("You selected some of them, lets specify your selection.")
		#will need more configuration
	elif stoploss_settings == "F":
		print("You selected none of them, crazy.")
	else:
		print("Input error. Please try again.\n")

def param_selection_define(selecs):
	if selecs == "A":
		print("You chose changing all parameters, lets go!")
		profit_taking_config()
		profit_target_config()
		rebalancing_config()
		bag_sizing()
		fa_on()
		fa_passes_setting()
		stoploss_management() #maybe move this before FA options booth here and in the stated functions to make it match the flow stated in the question form
	elif selecs == "B":
		print("Alright, lets define what parameters you want to change")
	else:
		print("Input error, try not missing the a or b keys next time.")

param_selection_define(change_selection)
