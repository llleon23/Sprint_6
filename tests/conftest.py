import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from curl import *


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Firefox()
    driver.get(main_site)
    yield driver
    driver.quit()

