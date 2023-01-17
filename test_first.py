from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest


def setup_module(module):
    print("this is setup function")
@pytest.mark.smoke
def test_login():
    print("this is login test case")
    assert 1==1, "window size is not matches"
@pytest.mark.regression
def test_home_page():
    print("executing the home page test case")
    title = 'Ebay for shopping'
    assert 'Ebay' in title, 'ebay title not match'

@pytest.mark.smoke
def test_login_credo():
    print("excuting the login test case")
    login = False
    assert login==False,"user not in login page"

def teardown_module(module):
    print("this is teardown function")


@pytest.mark.parametrize("testcase", ['login', 'homepage'])
def test_case(testcase):
    print("the name is ", testcase)
