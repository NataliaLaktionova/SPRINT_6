import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators

@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(MainPageLocators.URL_app)
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()