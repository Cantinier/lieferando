import pytest
from config import DOMAIN_URL
from selenium import webdriver
from Drivers.router import get_path
import pytest
from Steps.MainPage.MainPageSteps import get_cookie_banner_button


@pytest.fixture(scope="function")
def get_driver(request):
    driver = webdriver.Chrome(get_path())
    driver.get(DOMAIN_URL)
    cookie_button = get_cookie_banner_button(driver)
    if cookie_button:
        cookie_button.click()

    def close_browser():
        driver.close()

    request.addfinalizer(close_browser)
    return driver