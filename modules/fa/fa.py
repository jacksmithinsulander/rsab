import requests
import json
from modules.fa.chain_translator import translator

url1 = 'https://api.gopluslabs.io/api/v1/token_security/1?contract_addresses=0x2b591e99afe9f32eaa6214f7b7629768c40eeb39'
url2 = 'https://cfw.dexscreener.com/sc/dex:ethereum:0x9e0905249CeEFfFB9605E034b534544684A58BE6'
url3 = 'https://www.dextools.io/shared/data/pair?address=0x69d91b94f0aaf8e8a2586909fa77a5c2c89818d5&chain=ether&audit=true&locks=true'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Cookie': '_pk_ref.4.b299=%5B%22%22%2C%22%22%2C1687783998%2C%22https%3A%2F%2Ft.co%2F%22%5D; _pk_id.4.b299=ad4433ca8065d35b.1687783998.; _pk_ses.4.b299=1; __cf_bm=nzKBmFdipBO3WOZSCGc2uHpiWBytTCzAquJC1xYEmZk-1687786726-0-Af0dwaPEP2k1gm0IXWKEjCdwrKE79kIQsNNdIz1peQqeZQJjXBwtry0lKemsAQruY/+50I+HEd3ZZW2yvn6/bZvlTMP6VYXmwZEnKTnyqNKJ'
}

response1 = requests.get(url1)
response2 = requests.get(url2, headers=headers)
response3 = requests.get(url3, headers=headers)
print("Response1, ", response1.text)
print(" ")
print("#######################################################################")
print(" ")
print("Response2, ", response2.text)
print(" ")
print("#######################################################################")
print(" ")
print("Response3, ", response3.text)

goplus_url_base = 'https://api.gopluslabs.io/api/v1/token_security/'
dexscreener_url_base = 'https://cfw.dexscreener.com/sc/dex:'
dextools_url_base = 'https://www.dextools.io/shared/data/pair?address='

def goplus_fa(network, token):
	chain = translator(network)
	custom_url = goplus_url_base + chain + "?contract_addresses=" + token
	res = requests.get(custom_url)
	res_json = res.json()
	return res_json

def dexscreener_fa(network, pool):
	custom_url = dexscreener_url_base + network + ":" + pool
	res = requests.get(custom_url, headers=headers)
	res_json = res.json()	
	return res_json

#def dextools_fa(network, pool):

def full_fa(name, tokensniffer, dextools, token, lp, chain_short, chain_extra, chain):
	print("Name: ", name)
	print("Token: ", token)
	print("lp: ", lp)
	print("Chain short: ", chain_short)
	print("Chain extra: ", chain_extra)
	print("Chain: ", chain)
	goplus_analysis = goplus_fa(chain_short, token)
	print(goplus_analysis)
	dexscreener_analysis = dexscreener_fa(chain, lp)
	print(dexscreener_analysis)


