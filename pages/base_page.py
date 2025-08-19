from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from data.config import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(self.driver)

    def open(self):
        self.driver.get(BASE_URL)