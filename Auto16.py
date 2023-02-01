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
driver.get('https://jqueryui.com/draggable/')
link1 = driver.find_element(By.ID, "draggable")
act = ActionChains(link1)
act.move_by_offset(100,100).perform()