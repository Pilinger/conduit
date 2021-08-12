import time
# importing web driver waiting components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# clicking on decline button and checking if it disappears
#  calling fixture driver from conftest.py
def test_decline_cookies(driver):
    time.sleep(1)
    decline_xpath = '//div[@class="cookie__bar__buttons"]/button'
    """Wait or no"""
    decline_buttons = WebDriverWait(driver,
                                    10).until(EC.visibility_of_any_elements_located((By.XPATH, decline_xpath)))
    assert (len(decline_buttons) > 0)
    decline_buttons[0].click()
    time.sleep(1)
    decline_buttons = driver.find_elements_by_xpath(decline_xpath)
    assert (len(decline_buttons) == 0)
