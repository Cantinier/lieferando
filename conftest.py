import pytest
from config import DOMAIN_URL
from selenium import webdriver
from Drivers.router import get_path
import pytest


@pytest.fixture(scope="function")
def get_driver(request):
    driver = webdriver.Chrome(get_path())
    driver.get(DOMAIN_URL)

    def close_browser():
        driver.close()

    request.addfinalizer(close_browser)
    return driver