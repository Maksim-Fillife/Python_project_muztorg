from locators.instruments_page_locators import InstrumentLocators as locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random



class InstrumentsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def confirm_region(self):
        confirm_region = self.wait.until(
            EC.element_to_be_clickable(locators.CONFIRM_REGION_BUTTON)
        )
        confirm_region.click()

    def close_cookies(self):
        close_cooke_banner = self.wait.until(
            EC.element_to_be_clickable(locators.CLOSE_COOKIE_BANNER_BUTTON)
        )
        close_cooke_banner.click()

    def search_product(self, keyword):
        search_input = self.wait.until(
            EC.element_to_be_clickable(locators.SEARCH_INPUT)
        )
        search_input.click()
        search_input.send_keys(keyword)
        result_item = self.wait.until(
            EC.element_to_be_clickable(locators.SEARCH_SUGGEST_ITEM(keyword))
        )
        result_item.click()

    def check_search_result(self, keyword):
        result_search = self.wait.until(
            EC.visibility_of_element_located(locators.SEARCH_RESULT(keyword))
        )
        assert result_search.is_displayed()
        print(f'Найдено по запросу "{keyword}"')

    def open_catalog(self):
        catalog_button = self.wait.until(
            EC.element_to_be_clickable(locators.CATALOG_BUTTON)
        )
        catalog_button.click()

    def go_to_guitars_category(self):
        guitars_category = self.wait.until(
            EC.element_to_be_clickable(locators.GUITARS_CATEGORY_LINK)
        )
        guitars_category.click()

    def go_to_acoustic_guitars(self):
        acoustic_guitars_category = self.wait.until(
            EC.element_to_be_clickable(locators.ACOUSTIC_GUITARS_LINK)
        )
        acoustic_guitars_category.click()

    def go_to_electric_guitars(self):
        electric_guitars_category = self.wait.until(
            EC.element_to_be_clickable(locators.ELECTRIC_GUITARS_LINK)
        )
        electric_guitars_category.click()

    def check_category_title(self, title) :
        check_acoustic_guitars_page = self.wait.until(
            EC.visibility_of_element_located(locators.CATEGORY_TITLE(title))
        )
        assert check_acoustic_guitars_page.is_displayed()

    def select_random_card(self):
        cards = self.wait.until(
            EC.presence_of_all_elements_located(locators.PRODUCT_CARDS)
        )
        select_product_card = random.choice(cards)
        card_name_element = select_product_card.find_element(*locators.PRODUCT_CARD_NAME)
        card_name = card_name_element.text.strip()
        print(f"{card_name}")
        self.last_select_product = card_name
        return card_name

    def open_product_card(self):
        open_instrument = self.driver.find_element(*locators.OPEN_PRODUCT_CARD(self.last_select_product))
        open_instrument.click()

    def check_product_title(self):
        check_title = self.driver.find_element(*locators.PRODUCT_TITLE(self.last_select_product))
        assert check_title.is_displayed()

    def add_product_to_cart(self):
            add_product_to_cart = self.wait.until(
                EC.element_to_be_clickable(locators.ADD_TO_CART_BUTTON(self.last_select_product))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_product_to_cart)
            self.driver.execute_script("arguments[0].style.border='3px solid red';", add_product_to_cart)
            self.driver.execute_script("arguments[0].click();", add_product_to_cart)


    def check_cart_badge(self):
        cart_badge = self.wait.until(
            EC.visibility_of_element_located(locators.CART_BADGE)
        )
        assert cart_badge.text == "1"

    def open_cart(self):
        open_cart = self.wait.until(
            EC.element_to_be_clickable(locators.OPEN_CART_LINK)
        )
        open_cart.click()


    def check_product_in_cart(self):
        check_product_in_cart = self.wait.until(
            EC.visibility_of_element_located(locators.PRODUCT_NAME_IN_CART(self.last_select_product))
        )
        assert check_product_in_cart.is_displayed()

    def delete_product_from_cart(self):
        self.driver.find_element(By.TAG_NAME, "body").click()
        delete_product = self.wait.until(
            EC.element_to_be_clickable(locators.DELETE_PRODUCT_BUTTON)
        )
        delete_product.click()

    def check_empty_cart(self):
        empty_message = self.wait.until(
            EC.visibility_of_element_located(locators.EMPTY_CART_MESSAGE)
        )
        assert empty_message.is_displayed()

    def add_product_to_wishlist(self):
        add_to_wishlist = self.wait.until(
            EC.element_to_be_clickable(locators.ADD_TO_WISHLIST_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_wishlist)
        self.driver.execute_script("arguments[0].style.border='3px solid red';", add_to_wishlist)
        self.driver.execute_script("arguments[0].click();", add_to_wishlist)

    def open_wishlist(self):
        open_wishlist = self.wait.until(
            EC.visibility_of_element_located(locators.WISHLIST_LINK)
        )
        open_wishlist.click()

    def check_adding_to_wishlist(self):
        adding_to_wishlist = self.wait.until(
            EC.visibility_of_element_located(locators.WISHLIST_PRODUCT_NAME(self.last_select_product))
        )
        adding_to_wishlist.is_displayed()