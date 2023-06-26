import requests

# URL to send the GET request to
url1 = 'https://api.gopluslabs.io/api/v1/token_security/1?contract_addresses=0x2b591e99afe9f32eaa6214f7b7629768c40eeb39'
url2 = 'https://cfw.dexscreener.com/sc/dex:ethereum:0x4FF4c7c8754127Cc097910cf9D80400ADEf5b65d'
url3 = 'https://www.dextools.io/shared/data/pair?address=0x90d07a18f20e155d8e405181d8f6ec90ba5e7347&chain=bsc&audit=true&locks=true'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Cookie': '_pk_ref.4.b299=%5B%22%22%2C%22%22%2C1687783998%2C%22https%3A%2F%2Ft.co%2F%22%5D; _pk_id.4.b299=ad4433ca8065d35b.1687783998.; _pk_ses.4.b299=1; __cf_bm=nzKBmFdipBO3WOZSCGc2uHpiWBytTCzAquJC1xYEmZk-1687786726-0-Af0dwaPEP2k1gm0IXWKEjCdwrKE79kIQsNNdIz1peQqeZQJjXBwtry0lKemsAQruY/+50I+HEd3ZZW2yvn6/bZvlTMP6VYXmwZEnKTnyqNKJ'
}

# Sending the GET request and storing the response
response1 = requests.get(url1)
response2 = requests.get(url2, headers=headers)
response3 = requests.get(url3, headers=headers)
# Printing the response content
print("Response1, ", response1.text)
print(" ")
print("#######################################################################")
print(" ")
print("Response2, ", response2.text)
print(" ")
print("#######################################################################")
print(" ")
print("Response3, ", response3.text)
