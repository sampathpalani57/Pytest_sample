from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class Ebay():
    url = "https://www.ebay.com/"

    def setup(self):
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(2)

    def nav(self):
        driver.get(Ebay.url)

    def paginfo(self):
        title = driver.title
        Current_url = driver.current_url
        print("the current titile is:", title)
        print("the current URL is:", Current_url)

    def login_testcase(self):
        print("this is test case")

    def tear_down(self):
        driver.quit()


driver = webdriver.Chrome(ChromeDriverManager().install())
obj = Ebay()
obj.setup()
obj.nav()
obj.paginfo()
obj.login_testcase()
obj.tear_down()