import pytest
import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# importing web driver waiting components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# importing os for running docker-compose up -d
import os


# initialising driver
@pytest.fixture(scope='session')
def browser_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # os.system('docker-compose up -d')
    driver.get("http://localhost:1667/#/")
    return driver


# CON_TC_001_registration
def test_reg(browser_driver):
    time.sleep(1)
    register_xpath = '//a[@href="#/register"]'
    user_xpath = '//input[@placeholder="Username"]'
    user_li_xpath = '//*[@id="app"]/nav/div/ul/li[4]/a'
    email_xpath = '//input[@placeholder="Email"]'
    password_xpath = '//input[@placeholder="Password"]'
    user_name = 'testuser66'
    password_str = 'Abcd123$'
    email_end = '@example.com'
    sign_up = WebDriverWait(browser_driver, 10).until(EC.visibility_of_element_located((By.XPATH, register_xpath)))
    sign_up.click()
    time.sleep(1)
    user = WebDriverWait(browser_driver, 10).until(EC.visibility_of_element_located((By.XPATH, user_xpath)))
    user.send_keys(user_name)
    time.sleep(1)
    browser_driver.find_element_by_xpath(email_xpath).send_keys(f"{user_name}{email_end}")
    time.sleep(1)
    browser_driver.find_element_by_xpath(password_xpath).send_keys(password_str)
    time.sleep(1)
    browser_driver.find_element_by_xpath('//form/button').click()
    time.sleep(2)
    username = browser_driver.find_element_by_xpath(user_li_xpath).text
    assert (username == user_name)