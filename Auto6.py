
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service
import time
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://testautomationpractice.blogspot.com/")
title = driver.title
print("the page title is:", title)
Current_URL = driver.current_url
print("the current page uRL is:", Current_URL)
driver.switch_to.frame(0)
driver.find_element(By.ID, 'RESULT_FileUpload-10').send_keys("D://images/apple2.jpg")
time.sleep(4)
