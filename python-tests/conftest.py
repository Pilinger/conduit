import time
import pytest

# preparing selenium and chrome web driver manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# importing os for environmental variable, and docker-compose up
import os


# initialising driver for the whole session
@pytest.fixture(scope='session')
def driver():
    """Passing Chrome Driver"""
    URL = 'http://localhost:1667/#/'
    options = Options()
    # checking if headless mode is needed
    if os.getenv('HEADLESS'):
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    d = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # if headless mode is not defined, then it runs locally, docker needs to start up
    if not os.getenv('HEADLESS'):
        os.system('docker-compose up -d')
        time.sleep(24)
    d.get(URL)
    time.sleep(2)
    return d
