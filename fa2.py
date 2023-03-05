from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
import cloudscraper
import json

driver = uc.Chrome()

#Token info that we will fetch from the database
token_address = "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39"
token_chain_short = "eth"
token_chain = "ethereum"
token_chain_extra = "ether"
token_lp_pair = "0x9e0905249CeEFfFB9605E034b534544684A58BE6"

#Website links
tokensniffer_url = "https://tokensniffer.com/token/"
dextools_url = "https://www.dextools.io/app/en/"


def multi_fa(link, token, chain):
	if "tokensniffer" in link:
		site_url = link + chain + "/" + token
		element_xpath = '//*[@id="__next"]/div/main/div[2]/div[2]/div[1]/table[1]/tbody/tr[1]/td/h2/span'
	else:
		site_url = link + chain + "/pair-explorer/" + token
		element_xpath = '//*[@id="progressDext"]/div/div/strong'
	driver.get(site_url)
	fa_score = WebDriverWait(driver, timeout=40).until(
		EC.presence_of_element_located((By.XPATH, element_xpath))
	)
	result = fa_score.text
	if "/100" in result:
		result_int = int(result.removesuffix("/100"))
	else:
		result_int = int(result)
	print(result_int) 

multi_fa(tokensniffer_url, token_address, token_chain_short)
multi_fa(dextools_url, token_lp_pair, token_chain_extra)

def dexscreener_fa(token, chain):
	token_url = "https://cfw.dexscreener.com/sc/dex:" + chain + ":" + token + "/counter"
	scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
	r = scraper.get(token_url)
	y = json.loads(r.text)
	#Want to make this part more DRY by making a function that creates these through iteration
	scam_ratings = str(y["report"]["scam"]["total"])
	shit_ratings = str(y["rating"]["poop"]["total"])
	fire_rating = str(y["rating"]["fire"]["total"])
	moon_rating = str(y["rating"]["rocket"]["total"])
	print("scam ratings = " + scam_ratings + " And shit ratings = " + shit_ratings + " And fire = " + fire_rating + " And the moon is " + moon_rating)

dexscreener_fa(token_lp_pair, token_chain)

