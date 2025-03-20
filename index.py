from selenium import webdriver
import json

driver = webdriver.Chrome()
driver.get("https://ibkinsurance.blogspot.com/")

cookies = driver.get_cookies()
with open("cookies.json", "w") as f:
    json.dump(cookies, f, indent=4)

driver.quit()