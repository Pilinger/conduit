import time
# importing web driver waiting components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#  calling fixture driver from conftest.py instead

# CON_TC_001_registration
# registration of a new user
def test_reg(driver):
    time.sleep(2)
    # assigning the xpath texts
    register_xpath = '//a[@href="#/register"]'
    user_xpath = '//input[@placeholder="Username"]'
    user_li_xpath = '//*[@id="app"]/nav/div/ul/li[4]/a'
    email_xpath = '//input[@placeholder="Email"]'
    password_xpath = '//input[@placeholder="Password"]'
    # test data for registration
    user_name = 'testuser66'
    password_str = 'Abcd123$'
    email_end = '@example.com'
    sign_up_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, register_xpath)))
    sign_up_button.click()
    time.sleep(1)
    user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, user_xpath)))
    user.send_keys(user_name)
    time.sleep(1)
    driver.find_element_by_xpath(email_xpath).send_keys(f"{user_name}{email_end}")
    time.sleep(1)
    driver.find_element_by_xpath(password_xpath).send_keys(password_str)
    time.sleep(1)
    driver.find_element_by_xpath('//form/button').click()
    time.sleep(4)
    assert (driver.find_element_by_xpath('//div[@class="swal-title"]').text == 'Welcome!')
    assert (driver.find_element_by_xpath('//div[@class="swal-text"]').text == 'Your registration was successful!')
    driver.find_element_by_xpath('//button[text()="OK"]').click()
    time.sleep(2)
    username = driver.find_element_by_xpath(user_li_xpath).text
    assert (username == user_name)
