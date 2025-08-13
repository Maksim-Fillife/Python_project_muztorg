from selenium.webdriver.common.by import By

class InstrumentLocators:

    # Поисковая строка
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Искать на Музторг']")
    SEARCH_SUGGEST_ITEM = lambda search_text: (By.XPATH, f"//b[text()='{search_text}']")
    SEARCH_RESULT = lambda search_text: (By.XPATH, f"//span[contains(text(), '{search_text}')]")

    # Баннеры и модалки
    CONFIRM_REGION_BUTTON = (By.CSS_SELECTOR, "div[class='subheader__region'] button[class='mt-button _medium _red js-region-yes']")
    CLOSE_COOKIE_BANNER_BUTTON = (By.CSS_SELECTOR, "button[class*='js-popup-cookie-close']")

    # Каталог
    CATALOG_BUTTON = (By.CSS_SELECTOR, "button.js-catalog-menu-button")
    GUITARS_CATEGORY_LINK = (By.CSS_SELECTOR, "a[href='/category/gitary']")
    ACOUSTIC_GUITARS_LINK = (By.CSS_SELECTOR, "div[title='Акустические гитары']")
    ELECTRIC_GUITARS_LINK = (By.CSS_SELECTOR, "div[title='Электрогитары']")
    CATEGORY_TITLE = lambda text: (By.XPATH, f"//h1[contains(text(),'{text}')]")

    # # Карточка товара
    OPEN_PRODUCT_CARD = lambda card_name: (By.XPATH, f"//a[contains(@class, 'catalog-card__name') and text()=\"{card_name}\"]")
    PRODUCT_TITLE = lambda card_name: (By.XPATH, f"//h1[@class='title-1' and text()='{card_name}']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "article.catalog-card.js-catalog-card[itemtype*='Product']")
    PRODUCT_CARD_NAME = (By.CSS_SELECTOR, ".catalog-card__name")
    # PRODUCT_CARD_PRICE = (By.CSS_SELECTOR, ".catalog-card__price ")
    #
    # # Корзина
    ADD_TO_CART_BUTTON = lambda card_name: (By.XPATH, f"//a[contains(@class, '_red') and @data-role='add-to-cart' and @data-title=\"{card_name}\"]")
    CART_BADGE = (By.XPATH, "//span[contains(@class, 'js-header-amount')]")
    OPEN_CART_LINK = (By.CSS_SELECTOR, "a.mt-header__link[href='/cart/index']")
    PRODUCT_NAME_IN_CART = lambda card_name: (By.XPATH, f"//a[contains(@class, 'cart-list__name') and contains(., '{card_name}')]")
    DELETE_PRODUCT_BUTTON = (By.XPATH, "//a[@data-role='delete-cart' and @class='cart-list__trash']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//h1[text()='В Корзине пока нет товаров']")

    # Избранное
    ADD_TO_WISHLIST_BUTTON = (By.XPATH, "//button[@title='Добавить в избранное' and contains(@class, '_wishlist')]")
    WISHLIST_LINK = (By.XPATH, "//a[@href='/favorites' and contains(., 'Избранное')]")
    WISHLIST_PRODUCT_NAME = lambda card_name: (By.XPATH, f"//a[@class='catalog-card__name' and text()='{card_name}']")