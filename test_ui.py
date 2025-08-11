import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pytest




def test_search_musical_instrument_by_keyword(driver):
    driver.get("https://www.muztorg.ru/")
    wait = WebDriverWait(driver, 10)
    search_text = 'gibson'
    search_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Искать на Музторг']"))
    )
    search_input.click()
    search_input.send_keys(search_text)
    result_item = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//b[text()='{search_text}']"))
    )
    result_item.click()
    result_search = wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{search_text}')]"))
    )
    assert result_search.is_displayed()

def test_navigate_to_acoustic_guitars_category(driver):
    driver.get("https://www.muztorg.ru/")
    wait = WebDriverWait(driver, 10)
    catalog_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.js-catalog-menu-button"))
    )
    catalog_button.click()
    guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category/gitary']"))
    )
    guitars_category.click()
    acoustic_guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Акустические гитары']"))
    )
    acoustic_guitars_category.click()
    check_acoustic_guitars_page = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.category-head__title"))
    )
    assert check_acoustic_guitars_page.is_displayed()

def test_open_product_card(driver):
    driver.get("https://www.muztorg.ru/")
    wait = WebDriverWait(driver, 10)
    catalog_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.js-catalog-menu-button"))
    )
    catalog_button.click()
    guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category/gitary']"))
    )
    guitars_category.click()
    acoustic_guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Акустические гитары']"))
    )
    acoustic_guitars_category.click()

    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.catalog-card.js-catalog-card[itemtype*='Product']"))
    )
    select_product_card = random.choice(cards)
    card_name_element = select_product_card.find_element(By.CSS_SELECTOR, ".catalog-card__name")
    card_name = card_name_element.text.strip()
    print(f"{card_name}")

    card_price_element = select_product_card.find_element(By.CSS_SELECTOR, ".catalog-card__price ")
    card_price = card_price_element.text.strip()
    print(f"{card_price}")

    open_product = driver.find_element(By.XPATH, f"//a[contains(@class, 'catalog-card__name') and text()='{card_name}']")
    open_product.click()

    check_title = driver.find_element(By.XPATH, f"//h1[@class='title-1' and text()='{card_name}']")
    assert check_title.is_displayed()

    # check_price = driver.find_element(By.XPATH, f"//div[@class='mt-product-price__discounted-value'][contains(text(), '{card_price}')]")
    # assert check_price.is_displayed()

def test_add_product_to_cart(driver):
    driver.get("https://www.muztorg.ru/")
    wait = WebDriverWait(driver, 10)
    catalog_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.js-catalog-menu-button"))
    )
    catalog_button.click()
    guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category/gitary']"))
    )
    guitars_category.click()
    acoustic_guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Акустические гитары']"))
    )
    acoustic_guitars_category.click()

    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.catalog-card.js-catalog-card[itemtype*='Product']"))
    )
    select_product_card = random.choice(cards)
    card_name_element = select_product_card.find_element(By.CSS_SELECTOR, ".catalog-card__name")
    card_name = card_name_element.text.strip()
    print(f"{card_name}")

    open_product = driver.find_element(By.XPATH, f"//a[contains(@class, 'catalog-card__name') and contains(text(), '{card_name}')]")
    open_product.click()

    add_product_to_cart = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-role='add-to-cart' and .//span[text()='В корзину']]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_product_to_cart)
    driver.execute_script("arguments[0].style.border='3px solid red';", add_product_to_cart)
    driver.execute_script("arguments[0].click();", add_product_to_cart)

    cart_badge = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'js-header-amount')]"))
    )
    assert cart_badge.text == "1"

def test_view_shopping_cart(driver):
    # Открываем сайт
    driver.get("https://www.muztorg.ru/")
    wait = WebDriverWait(driver, 10)

    #
    close_cooke_banner = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='js-popup-cookie-close']"))
    )
    close_cooke_banner.click()
    #
    catalog_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.js-catalog-menu-button"))
    )
    catalog_button.click()
    #
    guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category/gitary']"))
    )
    guitars_category.click()
    #
    acoustic_guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Акустические гитары']"))
    )
    acoustic_guitars_category.click()
    #
    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.catalog-card.js-catalog-card[itemtype*='Product']"))
    )
    select_product_card = random.choice(cards)
    card_name_element = select_product_card.find_element(By.CSS_SELECTOR, ".catalog-card__name")
    card_name = card_name_element.text.strip()
    print(f"{card_name}")
    #
    open_product = driver.find_element(By.XPATH, f"//a[contains(@class, 'catalog-card__name') and contains(text(), '{card_name}')]")
    open_product.click()
    #
    add_product_to_cart = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-role='add-to-cart' and .//span[text()='В корзину']]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_product_to_cart)
    driver.execute_script("arguments[0].style.border='3px solid red';", add_product_to_cart)
    driver.execute_script("arguments[0].click();", add_product_to_cart)

    cart_badge = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'js-header-amount')]"))
    )
    assert cart_badge.text == "1"

    open_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.mt-header__link[href='/cart/index']"))
    )
    open_cart.click()

    check_product_in_cart = wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//a[contains(@class, 'cart-list__name') and contains(., '{card_name}')]"))
    )
    assert check_product_in_cart.is_displayed()


def test_add_wishlist(driver):
    # Открываем сайт
    driver.get("https://www.muztorg.ru/")
    wait = WebDriverWait(driver, 10)
    #
    # # Подтверждаем геолокацию
    # confirm_region = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'js-region-yes')]"))
    # )
    # confirm_region.click()

    # соглашаемся с куки
    close_cooke_banner = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='js-popup-cookie-close']"))
    )
    close_cooke_banner.click()

    catalog_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.js-catalog-menu-button"))
    )
    catalog_button.click()
    #
    guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category/gitary']"))
    )
    guitars_category.click()
    #
    acoustic_guitars_category = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Акустические гитары']"))
    )
    acoustic_guitars_category.click()
    #
    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.catalog-card.js-catalog-card[itemtype*='Product']"))
    )
    select_product_card = random.choice(cards)
    card_name_element = select_product_card.find_element(By.CSS_SELECTOR, ".catalog-card__name")
    card_name = card_name_element.text.strip()
    print(f"{card_name}")
    #
    open_product = driver.find_element(By.XPATH, f"//a[contains(@class, 'catalog-card__name') and contains(text(), '{card_name}')]")
    open_product.click()

    add_to_wishlist = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Добавить в избранное' and contains(@class, '_wishlist')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_wishlist)
    driver.execute_script("arguments[0].style.border='3px solid red';", add_to_wishlist)
    driver.execute_script("arguments[0].click();", add_to_wishlist)

    open_wishlist = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/favorites' and contains(., 'Избранное')]"))
    )
    open_wishlist.click()

    check_adding_to_wishlist = wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//a[@class='catalog-card__name' and text()='{card_name}']"))
    )
    check_adding_to_wishlist.is_displayed()