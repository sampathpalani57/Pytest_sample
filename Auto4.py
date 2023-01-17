from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://jqueryui.com/draggable/')
driver.switch_to.frame(0)
source1 = driver.find_element_by_id('draggable')
action = ActionChains(driver)
action.drag_and_drop_by_offset(source1, 100, 100).perform()
time.sleep(5)
driver.get('https://jqueryui.com/droppable/')
driver.switch_to.frame(0)
source1 = driver.find_element_by_id('draggable')
target1 = driver.find_element_by_id('droppable')
actions2 = ActionChains(driver)
actions2.drag_and_drop(source1, target1).perform()
time.sleep(5)
assertEqual("Dropped!", target1.text)
time.sleep(2)
driver.execute_script()
option = webdriver.ChromeOptions
option.add_argument("ing")