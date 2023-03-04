from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#Makes the browser stay open, might remove
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
	options=options)

driver.get("https://www.dextools.io/app/en/ether/pair-explorer/0xf29450019834d7874b4e306275c4334326ac27f1")
