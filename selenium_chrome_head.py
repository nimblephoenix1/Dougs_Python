from selenium import webdriver

DRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')



