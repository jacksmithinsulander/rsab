import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
#import requests
import cloudscraper

driver = uc.Chrome()


#driver.get("https://tokensniffer.com/token/eth/0x2b591e99afe9f32eaa6214f7b7629768c40eeb39")
token_address = "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39"
token_chain_short = "eth"
token_chain = "ethereum"

def tokensniffer_fa(token, chain):
	driver.get("https://tokensniffer.com/token/" + chain + "/" + token)
	tokensniffer_score = WebDriverWait(driver, timeout=40).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[1]/table[1]/tbody/tr[1]/td/h2/span'))
	)
	print(tokensniffer_score.text)

tokensniffer_fa(token_address, token_chain_short)

def dexscreener_fa(token, chain):
	#driver.get("https://cfw.dexscreener.com/sc/dex:" + chain + ":" + token)
	token_url = "https://cfw.dexscreener.com/sc/dex:" + chain + ":" + token + "/counter"
	scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
	r = scraper.get(token_url)
	#data = r.json
	print(r.text)

dexscreener_fa(token_address, token_chain)
