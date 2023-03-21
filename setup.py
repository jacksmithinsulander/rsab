import os.path
import json

class Object:
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__,
			sort_keys=True, indent=4)

default = Object()
default.profitSizePercentages = 50
default.profitTargets = 100
default.rebalancing = "true"
default.bagSizing = Object()
default.bagSizing.type  =  "dynamic"
default.bagSizing.universalSize = 1
default.stoplossManagement = Object()
default.stoplossManagement.type =  "200MA"
default.fa = "true"
default.faStrictness = 2

def profit_taking_config():
	print("=======================================================================")
	profit_taking = input('How many % profits do you want to take on each target levels? Answer with numbers ended by % sign, i.e. "50 %" or "100 %"(if you want to sell it all on first target)\n')
	if (profit_taking[:-2].isdigit() and 
		int(profit_taking.removesuffix(" %")) <= 100):
		print("Yes!")
		return int(profit_taking.removesuffix(" %"))
	else:
		print("Something went wrong, retry")

def profit_target_config():
	print("=======================================================================")
	tp = input('Standard profit taking is each time the worth of what you hold is worth double of what you initially bought. So if you bought for $10, the bot will take profit each time the bag is worth $20. How many % gains would you prefer for each profit taking? answer with numbers ended by % sign. \n')
	if tp[:-2].isdigit():
		print("Perfect!")
		return int(tp.removesuffix(" %"))
	else:
		print("Something went wrong, retry")

def rebalancing_config():
	print("=======================================================================")
	want_rebalancing = input('Do you want autorebalancing? (Y / N) \n')
	if want_rebalancing == "Y":
		print("Rebalancing is ON")
		return 1
	elif want_rebalancing == "N":
		print("Rebalancing is OFF")
		return 0

def bag_sizing():
	print("=======================================================================")
	dynamic_or_static = input("For bagsizing, would you like each bag to be (A) a dynamic %age of the ammount of dry powder your wallet holds or (B) a static number? Examples: Every time buy for 1 % of the dry powder or everytime buy for 1 dollar no matter what\n")
	sizing = Object()
	if dynamic_or_static == "A":
		dynamic_size = input("You chose dynamic bag sizing. How many percentages should each buy be?\n")
		sizing.type = "dynamic"
		sizing.universalSize =  int(dynamic_size.removesuffix(" %"))
	elif dynamic_or_static == "B":
		static_size = input("You chose static bag sizing. How many biden bucks would you like to gamble for each trade?\n")
		sizing.type = "static"
		sizing.universalSize = int(static_size.removesuffix(" %"))
	return sizing

def fa_on():
	print("=======================================================================")
	fa_toggle = input("FA (A) on or (B) off? (NOT RECOMENDED TO TURN OFF SINCE ITS ONLY CHECKING WETHER OR NOT YOU CAN ACTUALLY SELL THE SHITCOINS)\n")
	if fa_toggle == "A":
		print("FA is turned on")
		return 1
	elif fa_toggle == "B":
		print("FA is turned off")
		return 0

def fa_passes_settings():
	print("=======================================================================")
	fa_passes = input("The standard amount of passes for the 3 FA parameters are 2/3. Would you like to make it (A) 1/3, (B) 3/3 or (C) leave it as is?\n")
	if fa_passes == "A":
		print("1/3")
		return 1
	elif fa_passes == "B":
		print("3/3")
		return 3
	elif fa_passes == "C":
		print("2/3")
		return 2

def set_static_stoploss():
	stoploss = input("How many % loss would you like your stoploss to be at?\n")
	stoploss_obj = Object()
	stoploss_obj.type = "static"
	stoploss_obj.percentLoss = stoploss
	return stoploss_obj
	
def set_timebased_stoploss():
	deadline = input("How many days would you like to hold the shitcoin for?\n")
	deadline_obj = Object()
	deadline_obj.type = "days"
	deadline_obj.durationInDays = deadline
	return deadline_obj

def sl_chooser():
	print('Please specify what options youd like, sepparate them with ", " (commas that is)')
	sl_param_choose = input("(A) 200MA, (B) static stoploss or (C) timebased stoploss\n")
	sl_arr = sl_param_choose.split(", ")
	return sl_arr

def tryVar(var):
	try:
		val = var
	except NameError:
		return None
	return val

def stoploss_management():
	print("=======================================================================")
	stoploss_settings = input("The alternatives for potential stoplosses are (A) stoploss on the 200MA on the 4hr chart, (B) a static stoploss, (C) a timebased stoploss, (D) all of them, (E) some of them or (F) none of them. \n")
	if stoploss_settings == "A":
		print("You selected 200MA stoploss")
		stoploss_conf = Object()
		stoploss_conf.type = "200MA"
	elif stoploss_settings == "B":
		print("You selected a static stoploss")
		stoploss_conf = set_static_stoploss()
	elif stoploss_settings == "C":
		print("You selected a timebased stoploss")
		stoploss_conf = set_timebased_stoploss
	elif stoploss_settings == "D":
		print("You selected all of the options.")
		stoploss_conf = []
		trailing_sl = Object()
		trailing_sl.type = "200MA"
		static_sl = set_static_stoploss()
		deadline_sl = set_timebased_stoploss()
		stoploss_conf.append(trailing_slm, static_sl, deadline_sl)
	elif stoploss_settings  == "E":
		print("You selected some of them, lets specify your selection.")
		sl_selection = sl_chooser()
		stoploss_conf = []
		for x in sl_selection:
			if x == "A":
				trailing_sl = Object()
				trailing_sl.type = "200MA"
			elif x == "B":
				static_sl = set_static_stoploss()
			elif x == "C":
			 	deadline_sl = set_timebased_stoploss()
		if tryVar(trailing_sl) is None:
			 stoploss_conf.append(trailing_sl)
		if tryVar(static_sl) is None:
			stoploss_conf.append(static_sl)
		if tryVar(deadline_sl) is None:
			stoploss_conf.append(deadline_sl)		
	elif stoploss_settings == "F":
		print("You selected none of them, crazy.")
		stoploss_conf = Object()
		stoploss_conf.type = "none"
	else:
		print("Input error. Please try again.\n")
	return stoploss_conf

def spec_params():
	print("=======================================================================")
	print("What parameters would you like to tweak, ser?")
	print('Answer with just numbers, separated by commas i.e. "1, 2, 3" etc ')
	choosen_params = input("Profit taking size (1), profit targets (2), purchasing asset rebalancing (3), bag sizing (4), FA on off toggle (5), FA strictness (6), stoploss management (7)\n")
	params_arr = choosen_params.split(", ")
	return params_arr

def custom_choose():
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
	print("=======================================================================")
	change_selection = input("Do you want to change all of these parameters (A) or only some (B) of them?\n")
	if change_selection == "A":
		return 0
	elif change_selection == "B":
		return 1

#add recursion for retrys like this https://stackoverflow.com/questions/12828771/how-to-go-back-to-first-if-statement-if-no-choices-are-valid

def conf_tinker():
	conf_specify = custom_choose()
	if bool(conf_specify):
		print("Alright, lets define what parameters you want to change")
		params = spec_params()
		inverse_params = ["1", "2", "3", "4", "5", "6", "7"]
		for x in params:
			if x == "1":
				profit_taking = profit_taking_config()
				inverse_params.remove("1")
			elif x == "2":
				tp = profit_target_config()
				inverse_params.remove("2")
			elif x == "3":
				rebalance = rebalancing_config()
				inverse_params.remove("3")
			elif x == "4":
				bag = bag_sizing()
				inverse_params.remove("4")
			elif x == "5":
				fa = fa_on()
				inverse_params.remove("5")
			elif x == "6":
				fa_passes = fa_passes_settings()
				inverse_params.remove("6")
			elif x == "7":
				sl = stoploss_management()
				inverese_params.remove("7")
		for y in inverse_params:
			if y == "1":
				profit_taking = default.profitSizePercentages
			elif y == "2":
				tp = default.profitTargets
			elif y == "3":
				rebalance = default.rebalancing
			elif y == "4":
				bag = default.bagSizing
			elif y == "5":
				fa = default.fa
			elif y == "6":
				fa_passes = default.faStrictness
			elif y == "7":
				sl = default.stoplossManagement
	elif not bool(conf_specify):
		print("You chose changing all parameters, lets go!")
		profit_taking = profit_taking_config()
		tp = profit_target_config()
		rebalance = rebalancing_config()
		bag = bag_sizing()
		fa = fa_on()
		fa_passes = fa_passes_settings()
		sl = stoploss_management()
	tinker_results = [profit_taking, tp, rebalance, bag, fa, fa_passes, sl]
	return tinker_results

def param_choose_results():
	print("=======================================================================")
	print("Ait, now for the trading bot parameters, such as stop loss and profit taking")
	param_choose = input("Do you want the standard (1) or custom (2) settings?\n")
	if param_choose == "1":
		print("You selected the standard settings. wagmi")
		return 0
	elif param_choose == "2":
		print("You want to be adventurous and tinker with you own settings")
		return 1
	else:
		print("Didnt understand your input, try again\n")

def chain_chooser():
	print("Hello you filthy, degenerate ape. Lets set up this shitcoinbot of yours")
	print("=======================================================================")
	print('First of what EVMs would you like to "trade"(read gamble) on? Answer with the coresponding capitalized letters, separated by commas')
	chains = input("Ethereum mainnet (E), Arbitrum (A), Optimism (O), Polygon (P), Avalanche (V), Fantom (F), Binance smart chain (B) or ALL (ALL)\n")
	chainarr = chains.split(", ")
	chainarr_formatted = [] 
	for x in chainarr:
		if x == "E":
			chainarr_formatted.append("eth")
		elif x == "A":
			chainarr_formatted.append("arb")
		elif x == "O":
			chainarr_formatted.append("op")
		elif x == "P":
			chainarr_formatted.append("matic")
		elif x == "V":
			chainarr_formatted.append("avax")
		elif x == "F":
			chainarr_formatted.append("ftm")
		elif x == "B":
			chainarr_formatted.append("bnb")
		elif x == "ALL":
			print("You choose all")
		else:
			print("Input error. Please try again.\n")
	return chainarr_formatted

def conf_setup():
	chains = chain_chooser()
	print("Choosen chains are:")
	print(chains)
	params = param_choose_results()
	if bool(params):
		print("Lets tinker")
		tinker_results = conf_tinker()
		print(tinker_results)
		configuration = Object()
		configuration.profitSizePercentages = tinker_results[0]
		configuration.profitTargets = tinker_results[1]
		configuration.rebalancing = bool(tinker_results[2])
		configuration.bagSizing = tinker_results[3]
		configuration.fa = bool(tinker_results[4])
		configuration.faStrictness = tinker_results[5]
		configuration.stoplossManagement = tinker_results[6] 
	elif not bool(params):
		print("Standard setup")
		configuration = default
	configuration.chains = chains
	print(configuration.toJSON())
	f = open("conf.json", "x")
	f.write(configuration.toJSON())
	f.close

check_file = os.path.isfile("./conf.json")

def conf_checker(file_exists):
	if file_exists:
		print("Configuration file already exists")
	else:
		print("Conf-file does not exist")
		print("Let's set it up!")
		conf_setup()

conf_checker(check_file)
