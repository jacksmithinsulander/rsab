from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
import cloudscraper
import json

options = webdriver.ChromeOptions()
uc_options = uc.ChromeOptions()

uc_options.binary_location = '/home/ted/.local/share/undetected_chromedriver/undetected_chromedriver'

driver = uc.Chrome(options=options, chrome_options=uc_options)

# Token info that we will fetch from the database
# token_address = "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39"
# token_chain_short = "eth"
# token_chain = "ethereum"
# token_chain_extra = "ether"
# token_lp_pair = "0x9e0905249CeEFfFB9605E034b534544684A58BE6"
# token_name = "Hex"

# Website links
# tokensniffer_url = "https://tokensniffer.com/token/"
# dextools_url = "https://www.dextools.io/app/en/"


def multi_fa(link, token, chain):
    if "tokensniffer" in link:
        site_url = link + chain + "/" + token
        element_xpath = '//*[@id="__next"]/div/main/div[2]/div[2]/div[1]/table[1]/tbody/tr[1]/td/h2/span'
    else:
        site_url = link + chain + "/pair-explorer/" + token
        element_xpath = '//*[@id="progressDext"]/div/div/strong'
    driver.get(site_url)

    fa_score = WebDriverWait(driver, timeout=40).until(
        EC.presence_of_element_located((By.XPATH, element_xpath)))

    #   try:
    #     fa_score = WebDriverWait(driver, timeout=40).until(
    #         EC.presence_of_element_located((By.XPATH, element_xpath)))
    # except Exception:
    #     print("token not found on tokensniffer")
    #     is_passed = 0
    #     return is_passed

    if "/100" in fa_score.text:
        result_int = int(fa_score.text.removesuffix("/100"))
    else:
        result_int = int(fa_score.text)

    if result_int >= 70:
        is_passed = 1
    else:
        is_passed = 0
    return is_passed


def dexscreener_fa(token, chain):
    token_url = "https://cfw.dexscreener.com/sc/dex:" + \
        chain + ":" + token + "/counter"
    scraper = cloudscraper.create_scraper(
        delay=10,   browser={'custom': 'ScraperBot/1.0', })
    r = scraper.get(token_url)
    y = json.loads(r.text)
    # Wanna add a separate function that  creates these ratings though some kind of iteration
    scam_ratings = y["report"]["scam"]["total"]
    shit_ratings = y["rating"]["poop"]["total"]
    fire_ratings = y["rating"]["fire"]["total"]
    moon_ratings = y["rating"]["rocket"]["total"]
    bear_ratings = scam_ratings + shit_ratings
    bull_ratings = fire_ratings + moon_ratings
    if bull_ratings >= (bear_ratings * 1.5):
        is_passed = 1
    else:
        is_passed = 0
    return is_passed


def full_fa(name, tokensniffer, dextools, token, lp, chain_short, chain_extra, chain):
    try:
        tokensniffer_result = multi_fa(tokensniffer, token, chain_short)
        print("tokensniffer checked for token: " + name)
    except Exception:
        print("err tokensniffer for token: " + name)
        tokensniffer_result = 0
    try:
        dextools_result = multi_fa(dextools, lp, chain_extra)
        print("dextools checked for token: " + name)
    except Exception:
        print("err dextools for token: " + name)
        dextools_result = 0
    try:
        dexscreener_result = dexscreener_fa(lp, chain)
        print("dexscreener checked for token: " + name)
    except Exception:
        print("err dexscreener for token: " + name)
        dexscreener_result = 0
    full_result = tokensniffer_result + dextools_result + dexscreener_result
    print("Token " + name + " passed " + str(full_result) + "/3")
    return full_result

# full_fa(token_name, tokensniffer_url, dextools_url, token_address,
#         token_lp_pair, token_chain_short, token_chain_extra, token_chain)
