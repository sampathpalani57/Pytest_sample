from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.delete_all_cookies()
driver.get('https://demo.guru99.com/test/newtours/')
title = driver.title
print("the page title is:", title)
Current_URL = driver.current_url
print(Current_URL)
"""drop_down = driver.find_elements(By.CLASS_NAME, 'col-lg-3')
#select_value = Select(drop_down)
#select_value.select_by_index(2)
for drop_downs in drop_down:
    print("the drop_down values:", drop_downs)"""
driver.find_element(By.LINK_TEXT, "Security Project").click()

#window = driver.window_handles(1)
wait = WebDriverWait(driver, 10)
wait2 = wait.until(driver.find_element(By.LINK_TEXT, "Security Project"))
window = driver.window_handles
print('this is window details:', len(window))
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.frame()

