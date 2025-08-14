from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def auth_button(self):
        auth_button = self.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='header-auth']"))
    )
        self.action.move_to_element(auth_button).click().perform()

    def login_with_password(self):
        login_with_password = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.js-change-mode-to-login-by-password[data-mode='login-by-password']"))
        )
        login_with_password.click()

    def fill_email(self):
        fill_email = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-by-pass_phone-or-email-input']"))
        )
        self.action.move_to_element(fill_email).click().send_keys('lelrg@icloud.com').pause(1).perform()

    def fill_password(self):
        fill_password = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-by-pass_password-input']"))
        )
        self.action.move_to_element(fill_password).click().send_keys('ZXCASDqwe!@#123').pause(1).perform()

    def submit_button(self):
        submit_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='button button-orange _large js-login-form-submit-btn']"))
        )
        self.action.move_to_element(submit_button).click().perform()

    def check_message_error(self):
        error_message = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message']"))
        )
        error_message.is_displayed()

    def check_profile_button(self):
        profile_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'header-auth__menu')]//a[@class='mt-header__link']"))
        )
        profile_button.is_displayed()