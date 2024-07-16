from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

driver.get("https://www.google.com")

driver.find_element(By.NAME,'q').send_keys("amazon")
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").send_keys(Keys.ENTER)



