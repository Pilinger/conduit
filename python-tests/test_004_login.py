# Generated by Selenium IDE, later modified
import time
# importing web driver waiting components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#  calling fixture driver from conftest.py instead


# CON_TC_002_login
# logging in and testing if the username appears correctly
def test_logging_in(driver):
    time.sleep(1)
    # assigning xpath strings, and test strings
    login_xpath = '//a[@href="#/login"]'
    email_xpath = '//input[@placeholder="Email"]'
    password_xpath = '//input[@placeholder="Password"]'
    user_li_xpath = '//*[@id="app"]/nav/div/ul/li[4]/a'
    user_name = 'testuser1'
    password_str = 'Abcd123$'
    email_end = '@example.com'
    """Wait or no"""
    login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_xpath)))
    # login = driver.find_element_by_xpath(login_xpath)
    login.click()
    time.sleep(1)
    driver.find_element_by_xpath(email_xpath).send_keys(f'{user_name}{email_end}')
    time.sleep(1)
    driver.find_element_by_xpath(password_xpath).send_keys(password_str)
    time.sleep(1)
    driver.find_element_by_xpath('//form/button').click()
    time.sleep(2)
    username = driver.find_element_by_xpath(user_li_xpath).text
    assert (username == user_name)





