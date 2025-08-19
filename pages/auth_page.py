from selenium.webdriver.support import expected_conditions as EC
from locators.aut_page_locators import AutLocators as locators
from data.config import EMAIL, PASSWORD, WRONG_PASSWORD
from pages.base_page import BasePage
import time


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def auth_button(self):
        auth_button = self.wait.until(
        EC.element_to_be_clickable(locators.INPUT_BUTTON)
    )
        self.action.move_to_element(auth_button).click().perform()

    def login_with_password(self):
        time.sleep(2)
        login_with_password = self.wait.until(
            EC.element_to_be_clickable(locators.LOGIN_WITH_PASSWORD_LINK)
        )
        login_with_password.click()

    def fill_email(self):
        time.sleep(1)
        email_input = self.wait.until(EC.element_to_be_clickable(locators.INPUT_EMAIL))
        self.action.move_to_element(email_input).click().perform()

        for char in EMAIL:
            self.action.send_keys(char).pause(0.18).perform()

    def fill_password(self):
        password_input = self.wait.until(EC.element_to_be_clickable(locators.INPUT_PASSWORD))
        self.action.move_to_element(password_input).click().perform()

        for char in PASSWORD:
            self.action.send_keys(char).pause(0.13).perform()

    def fill_wrong_password(self):
        wrong_password_input = self.wait.until(EC.element_to_be_clickable(locators.INPUT_PASSWORD))
        self.action.move_to_element(wrong_password_input).click().perform()

        for char in WRONG_PASSWORD:
            self.action.send_keys(char).pause(0.1).perform()

    def click_submit_button(self):
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
        profile_button = self.wait.until(EC.element_to_be_clickable(locators.PROFILE_BUTTON))
        profile_button.is_displayed()

    def click_logout(self):
        profile_button = self.wait.until(EC.element_to_be_clickable(locators.PROFILE_BUTTON))
        self.action.move_to_element(profile_button).perform()
        logout_button = self.wait.until(EC.element_to_be_clickable(locators.LOGOUT_BUTTON))
        self.action.move_to_element(logout_button).click().perform()

    def check_logout(self):
        logout = self.wait.until(EC.visibility_of_element_located(locators.INPUT_BUTTON))
        assert logout.text.strip() == "Войти"
