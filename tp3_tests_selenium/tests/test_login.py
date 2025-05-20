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
    username_form = driver.find_element(By.NAME, "username")
    password_form = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/form/button[@type='submit']")

    username_form.send_keys("admin")
    password_form.send_keys("password123")
    login_button.click()
    assert driver.current_url == "http://localhost:5000/dashboard"

def test_login_failure_wrong_password(driver):
    username_form = driver.find_element(By.NAME, "username")
    password_form = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/form/button[@type='submit']")

    username_form.send_keys("admin")
    password_form.send_keys("wrongpassword")
    login_button.click()
    assert driver.find_element(By.XPATH, "/html/body/p").text == "Identifiants incorrects."

def test_login_empty_fields(driver):
    username_form = driver.find_element(By.NAME, "username")
    password_form = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/form/button[@type='submit']")

    username_form.send_keys("")
    password_form.send_keys("")
    login_button.click()

    assert driver.find_element(By.XPATH, "/html/body/p").text == "Tous les champs sont requis."
