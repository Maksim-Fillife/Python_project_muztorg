from selenium.webdriver.common.by import By



class AutLocators:

    INPUT_BUTTON = (By.XPATH, "//a[.//span[text()='Войти']]")
    LOGIN_WITH_PASSWORD_LINK = (By.CSS_SELECTOR, "button.js-change-mode-to-login-by-password[data-mode='login-by-password']")
    INPUT_EMAIL = (By.XPATH, "//input[@id='login-by-pass_phone-or-email-input']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='login-by-pass_password-input']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='button button-orange _large js-login-form-submit-btn']")
    PROFILE_BUTTON = (By.XPATH, "//div[contains(@class,'header-auth__menu')]//a[@class='mt-header__link']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message']")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='mt-header__main js-header-main']//li[10]//a[1]")