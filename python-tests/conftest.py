import pytest

# preparing selenium and chrome web driver manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# importing os for environmental variable
import os


# initialising driver
@pytest.fixture(scope='session')
def driver():
    """Passing Chrome Driver"""
    options = Options()
    # checking if headless mode is needed
    if os.getenv('HEADLESS'):
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    d = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # os.system('docker-compose up -d')
    d.get("http://localhost:1667/#/")
    return d
