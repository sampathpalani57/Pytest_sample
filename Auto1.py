from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get('https://www.guru99.com/select-option-dropdown-selenium-webdriver.html#3-selectbyindex-and-deselectbyindex')
title = driver.title
print("the page title is:", title)
Current_URL = driver.current_url
print("the current page uRL is:", Current_URL)
"""driver.find_element(By.ID, 'email').send_keys('sampath')
driver.find_element(By.NAME, 'pass').send_keys('sumo')
driver.find_element(By.LINK_TEXT, 'Forgotten password?').click()"""
#driver.find_element(By.CSS_SELECTOR, 'a[target="_blank"]').click()
#driver.find_element(By.CSS_SELECTOR, 'a[role^="link"]').click()
#driver.find_element(By.XPATH, '//input[@aria-label="Email address or mobile number"]').send_keys('this is sampath')
