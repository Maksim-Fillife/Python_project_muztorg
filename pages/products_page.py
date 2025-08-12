from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.products_locators import ProductLocators
import random

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.muztorg.ru/")
        wait = WebDriverWait(self.driver, 10)

    def confirm_region(self):
        confirm_region = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "div[class='subheader__region'] button[class='mt-button _medium _red js-region-yes']"))
        )
        confirm_region.click()