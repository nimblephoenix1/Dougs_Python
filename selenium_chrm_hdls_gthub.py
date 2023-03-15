
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.github.com/login")
print(driver.page_source)

#Send the user name to the user name login field
username = "nimblephoenix1"
uname = driver.find_element("id", "login_field") 
uname.send_keys( username )

#Send the password to the password field
psswrd 	= "&&10Doug##GH"
pw = driver.find_element("id", "password") 
pw.send_keys( psswrd )

#Find and click the 'sign in' button
driver.find_element("name", "commit").click()

# Wait for login process to complete.
WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))

error_message = "Incorrect username or password."
# Retrieve any errors found. 
errors = driver.find_elements(By.CLASS_NAME, "flash-error")

# When errors are found, the login will fail. 
if any(error_message in e.text for e in errors): 
    print("[!] Login failed")
else:
    print("[+] Login successful")

driver.close()