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
