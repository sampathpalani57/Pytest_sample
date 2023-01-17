import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest



@pytest.mark.usefixtures("before_function", "before_module")
@pytest.mark.regression
def test_login():
    print("testing login page")


@pytest.fixture(scope='function')
def before_function():
    print('launching the browser')
    yield
    print('quiting browser')
@pytest.fixture(scope='module')
def before_module():
    print('reading the data')
    yield
    print('closeing the data')

