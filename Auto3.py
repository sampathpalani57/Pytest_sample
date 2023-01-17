from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


option = webdriver.ChromeOptions()
option.add_argument("incognito")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
time.asctime()
driver.delete_all_cookies()
driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
title = driver.title
print("the page title is:", title)
Current_URL = driver.current_url
print(Current_URL)