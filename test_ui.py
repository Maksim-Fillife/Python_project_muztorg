import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By





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

    # confirm_region = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[text()='Да, верно']"))
    # )
    # confirm_region.click()

    check_title = driver.find_element(By.XPATH, f"//h1[@class='title-1' and text()='{card_name}']")
    assert check_title.is_displayed()

    # check_price = driver.find_element(By.XPATH, f"//div[@class='mt-product-price__discounted-value'][contains(text(), '{card_price}')]")
    # assert check_price.is_displayed()


