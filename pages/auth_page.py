from selenium.webdriver.support import expected_conditions as EC
from locators.aut_page_locators import AutLocators as locators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def auth_button(self):
        auth_button = self.wait.until(
        EC.element_to_be_clickable(locators.INPUT_BUTTON)
    )
        self.action.move_to_element(auth_button).click().perform()

    def login_with_password(self):
        login_with_password = self.wait.until(
            EC.element_to_be_clickable(locators.LOGIN_WITH_PASSWORD_LINK)
        )
        login_with_password.click()

    def fill_email(self):
        fill_email = self.wait.until(
            EC.element_to_be_clickable(locators.INPUT_EMAIL)
        )
        self.action.move_to_element(fill_email).click().send_keys('lelrg@icloud.com').pause(1).perform()

    def fill_password(self):
        fill_password = self.wait.until(
            EC.element_to_be_clickable(locators.INPUT_PASSWORD)
        )
        self.action.move_to_element(fill_password).click().send_keys('ZXCASDqwe!@#123').pause(1).perform()

    def submit_button(self):
        submit_button = self.wait.until(
            EC.element_to_be_clickable(locators.SUBMIT_BUTTON)
        )
        self.action.move_to_element(submit_button).click().perform()

    def check_message_error(self):
        error_message = self.wait.until(
            EC.visibility_of_element_located(locators.ERROR_MESSAGE)
        )
        error_message.is_displayed()

    def check_profile_button(self):
        profile_button = self.wait.until(
            EC.element_to_be_clickable(locators.PROFILE_BUTTON)
        )
        profile_button.is_displayed()