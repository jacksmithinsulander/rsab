import requests
import json
from modules.fa.chain_translator import translator

headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
	'Cookie': '_pk_ref.4.b299=%5B%22%22%2C%22%22%2C1687783998%2C%22https%3A%2F%2Ft.co%2F%22%5D; _pk_id.4.b299=ad4433ca8065d35b.1687783998.; _pk_ses.4.b299=1; __cf_bm=nzKBmFdipBO3WOZSCGc2uHpiWBytTCzAquJC1xYEmZk-1687786726-0-Af0dwaPEP2k1gm0IXWKEjCdwrKE79kIQsNNdIz1peQqeZQJjXBwtry0lKemsAQruY/+50I+HEd3ZZW2yvn6/bZvlTMP6VYXmwZEnKTnyqNKJ'
}

goplus_url_base = 'https://api.gopluslabs.io/api/v1/token_security/'
dexscreener_url_base = 'https://cfw.dexscreener.com/sc/dex:'
dextools_url_base = 'https://www.dextools.io/shared/data/pair?address='

def goplus_fa(network, token):
	chain = translator(network)
	custom_url = goplus_url_base + chain + "?contract_addresses=" + token
	res = requests.get(custom_url)
	res_json = res.json()
	token_data = res_json.get("result", {}).get(token.lower(), {})

	score = 0
	
	bull_variables = {
		"anti_whale": "is_anti_whale",
		"open_source": "is_open_source",
	}

	bear_variables = {
		"anti_whale_modifiable": "anti_whale_modifiable",
		"can_take_ownership": "can_take_back_ownership",
		"honeypot_detect": "is_honeypot",
		"honeypot_deployer": "honeypot_with_same_creator",
		"proxy": "is_proxy",
		"blacklist": "is_blacklisted",
		"transfer_pausable": "transfer_pausable",
		"mintable": "is_minteable"
	}

	creator_percent = token_data.get("creator_percent")
	holder_count = token_data.get("holder_count")

	if float(creator_percent) >= 0.1:
		score -= 5
	else:
		score += 5

	if int(holder_count) >= 100:
		score += 5
	else:
		score -= 5

	for var, key in bull_variables.items():
		value = token_data.get(key)
		if value == 1:
			score += 5
		else: 
			score -= 5
		
	for var, key in bear_variables.items():
		value = token_data.get(key)
		if value == 0:
			score += 5
		else: 
			score -= 5
	if score >= 0:
		is_passed = 1
	elif score <= 0:
		is_passed = 0
	return is_passed

def dexscreener_fa(network, pool):
	custom_url = dexscreener_url_base + network + ":" + pool + "/counter"
	res = requests.get(custom_url, headers=headers)
	res_json = res.json()
	n1 = res_json["report"]["scam"]["total"]
	n2 = res_json["rating"]["poop"]["total"]
	p1 = res_json["rating"]["fire"]["total"] 
	p2 = res_json["rating"]["rocket"]["total"]
	bull_ratings = p1 + p2
	bear_ratings = n1 + n2
	if bull_ratings >= (bear_ratings * 1.5):
		is_passed = 1
	elif bull_ratings <= (bear_ratings * 1.5):
		is_passed = 0
	return is_passed

def dextools_fa(network, pool):
	custom_url = (dextools_url_base + pool.lower() + "&chain=" + 
		network + "&audit=true&locks=true")
	res = requests.get(custom_url, headers=headers)
	res_json = res.json()
	dext_score = res_json["data"][0]["dextScore"]["total"]
	if dext_score >= 80:
		is_passed = 1
	elif dext_score <= 90:
		is_passed = 0
	return is_passed

def full_fa(name, token, lp, chain_short, chain_extra, chain):
	goplus_analysis = goplus_fa(chain_short, token)
	dexscreener_analysis = dexscreener_fa(chain, lp)
	dextools_analysis = dextools_fa(chain_extra, lp)
	full_result = (goplus_analysis + dexscreener_analysis + dextools_analysis)
	return full_result
