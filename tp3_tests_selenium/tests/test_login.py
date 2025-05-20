import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5000/login")
    yield driver
    driver.quit()

def test_login_success(driver):
    # TODO
    pass

def test_login_failure_wrong_password(driver):
    # TODO
    pass

def test_login_empty_fields(driver):
    # TODO
    pass
