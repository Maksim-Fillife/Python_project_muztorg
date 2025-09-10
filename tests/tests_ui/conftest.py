from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture(scope='function', autouse=True)
def driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    browser = webdriver.Chrome(options=options)

    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.execute_script("delete navigator.__proto__.webdriver")

    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.fixture
def instruments(driver):
    from pages.instruments_page import InstrumentsPage
    return InstrumentsPage(driver)

@pytest.fixture
def authorization(driver):
    from pages.auth_page import AuthPage
    return AuthPage(driver)