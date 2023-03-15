
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.wellsfargo.com/")
print(driver.page_source)
driver.quit()