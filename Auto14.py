from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.delete_all_cookies()
driver.maximize_window()
driver.get('https://login.yahoo.com/')
driver.find_element(By.ID, 'createacc').click()
time.sleep(2)
#window = driver.window_handles
#driver.switch_to.window(driver.window_handles[1])
test1 = driver.title
print(test1)
driver.back()
#driver.switch_to.window((driver.window_handles[0]))
#print(len(window))
test2 = driver.title
print(test2)
driver.quit()