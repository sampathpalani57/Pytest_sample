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
driver.get('https://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)
test = driver.find_element(By.ID, 'speed')
test2 = Select(test)
test3 = test2.select_by_visible_text("Faster")
test4 = test2.options
for i in test4:
    print(i.text)

driver.quit()