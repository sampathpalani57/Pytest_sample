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
driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
src = driver.find_element(By.CLASS_NAME, 'ui-widget-content ui-corner-tr ui-draggable ui-draggable-handle')
des = driver.find_element(By.CLASS_NAME, 'ui-widget-content ui-state-default ui-droppable')
#act =ActionChains(driver)
#ActionChains(driver).m
#link1.perform()
#driver.find_elements(By.XPATH, '//a[@title="Delete this image"]').
ActionChains.move_to_element(src).perform()

#ActionChains.drag_and_drop(des).perform()
link3 = driver.find_element(By.XPATH, "//a[@title='Delete this image']")
link3.click()
time.sleep(3)
driver.quit()