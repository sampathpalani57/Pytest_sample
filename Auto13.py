import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
XY = Select(driver.find_element(By.XPATH, "//select[@id='speed']"))
XY.select_by_visible_text("Medium")
XYZ= XY.options
print(len(XYZ))
for opt in XYZ:
    print(opt.text)