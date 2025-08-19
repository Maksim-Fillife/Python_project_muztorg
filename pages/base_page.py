from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
# from locators.aut_page_locators import AutLocators as locator
from data.config import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(self.driver)

    def open(self):
        self.driver.get(BASE_URL)

    def find_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def send_keys_human(self, locator, text, delay):
        element = self.find_element(locator)
        element.click()
        for char in text:
            self.action.send_keys(char).pause(delay).perform()

    def get_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text.strip()

    def hover(self, locator):
        element = self.find_element(locator)
        self.action.move_to_element(element).perform()