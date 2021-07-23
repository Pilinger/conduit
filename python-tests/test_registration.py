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
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # os.system('docker-compose up -d')
    driver.get("http://localhost:1667/#/")
    return driver


# CON_TC_001_registration
def test_reg(browser):
    time.sleep(1)
    sign_up = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="#/register"]')))
    sign_up.click()
    time.sleep(1)
    user = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '//input[@placeholder="Username"]')))
    user.send_keys('testuser66')
    time.sleep(1)
    browser.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testuser66@example.com")
    time.sleep(1)
    browser.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('Abcd123$')
    time.sleep(1)
    browser.find_element_by_xpath('//form/button').click()
    time.sleep(2)
    username = browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text
    assert (username == 'testuser66')
