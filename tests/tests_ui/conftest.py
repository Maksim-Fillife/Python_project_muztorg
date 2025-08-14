from selenium import webdriver
import pytest


@pytest.fixture(scope='function', autouse=True)
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.fixture
def instruments_page(driver):
    from pages.instruments_page import InstrumentsPage
    return InstrumentsPage(driver)