from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

#option = webdriver.ChromeOptions()
#option.add_argument("headless")
#option.add_argument("start_maximize")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
#driver.find_element(By.XPATH,"//a[contains(text(), 'SUPPORT')]").click()
#text = driver.find_element(By.XPATH, "//b[text()='sign-in here']").text
#print(text)
driver.switch_to.default_content()
frame1 = driver.find_element(By.NAME, 'SingleFrame')
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("sampath")
driver.switch_to.default_content()
test1 = driver.find_element(By.XPATH, "//h1[text()='Automation Demo Site ']").text
print(test1)
driver.implicitly_wait(3)

link1 = driver.find_element()
act = ActionChains(driver)
act.move_to_element(link2=link1)
act.perform()
