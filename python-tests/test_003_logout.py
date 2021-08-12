import time


# logging out after finishing the registration steps
#  calling fixture driver from conftest.py
def test_logout(driver):
    time.sleep(1)
    # signing out
    driver.find_element_by_xpath('//a[@active-class="active"]').click()
    time.sleep(2)
    # checking if login and register buttons appeared
    login_register = driver.find_elements_by_xpath('//a[@href="#/login" or @href="#/register"]')
    assert (len(login_register) > 0)
    # refreshing page to dispatch General Feed
    driver.refresh()
    time.sleep(2)
