from locators.aut_page_locators import AutLocators as locator
from data.config import EMAIL, PASSWORD, WRONG_PASSWORD
from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def auth_button(self):
        self.click(locator.INPUT_BUTTON)

    def login_with_password(self):
        self.click(locator.LOGIN_WITH_PASSWORD_LINK)

    def fill_email(self):
        self.send_keys_human(locator.INPUT_EMAIL, EMAIL, delay=0.1)

    def fill_password(self):
        self.send_keys_human(locator.INPUT_PASSWORD, PASSWORD, delay=0.1)

    def fill_wrong_password(self):
        self.send_keys_human(locator.INPUT_PASSWORD, WRONG_PASSWORD, delay=0.1)

    def click_submit_button(self):
        self.click(locator.SUBMIT_BUTTON)

    def check_message_error(self):
        self.find_visible_element(locator.ERROR_MESSAGE)

    def check_profile_button(self):
        self.find_visible_element(locator.PROFILE_BUTTON)

    def click_logout(self):
        self.hover(locator.PROFILE_BUTTON)
        self.click(locator.LOGOUT_BUTTON)

    def check_logout(self):
        actual_text = self.get_text(locator.INPUT_BUTTON)
        assert actual_text == "Войти"
