from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common import by
import time
from selenium.webdriver.chrome.service import service

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=r"../driver/chromedriver.exe")
driver.delete_all_cookies()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
driver.get_screenshot_as_file(r'C:\Users\sampa\pythonProject4\Helloworld\Automation project\screenshots\sampath.png')
driver.quit()