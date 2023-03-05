import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get("https://tokensniffer.com/token/eth/0x2b591e99afe9f32eaa6214f7b7629768c40eeb39")
#sleep(2)
score = WebDriverWait(driver, timeout=40).until(
	EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[2]/div[1]/table[1]/tbody/tr[1]/td/h2/span'))
)
#inal_score = [score.text for score in scores]
#score = driver.find_element(By.XPATH, )
print(score.text)
