


def test_valid_authorization(authorization, driver):
    authorization.open()
    authorization.auth_button()
    authorization.login_with_password()
    authorization.fill_email()
    authorization.fill_password()
    authorization.click_submit_button()

    # Отладка: что сейчас на экране?
    print("Current URL:", authorization.driver.current_url)
    print("Page Title:", authorization.driver.title)
    authorization.driver.save_screenshot("after_login.png")

    authorization.check_profile_button()

def test_authorization_with_wrong_password(authorization):
    authorization.open()
    authorization.auth_button()
    authorization.login_with_password()
    authorization.fill_email()
    authorization.fill_wrong_password()
    authorization.click_submit_button()
    authorization.check_message_error()

def test_logout(authorization):
    authorization.open()
    authorization.auth_button()
    authorization.login_with_password()
    authorization.fill_email()
    authorization.fill_password()
    authorization.click_submit_button()
    authorization.click_logout()
    authorization.check_logout()

def test_search_musical_instrument_by_keyword(instruments):
    instruments.open()
    instruments.search_product('fender')
    instruments.check_search_result('fender')

def test_navigate_to_acoustic_guitars_category(instruments):
    instruments.open()
    instruments.open_catalog()
    instruments.go_to_guitars_category()
    instruments.go_to_acoustic_guitars()
    instruments.check_category_title('Акустические гитары')

def test_open_product_card(instruments):
    instruments.open()
    instruments.confirm_region()
    instruments.close_cookies()
    instruments.open_catalog()
    instruments.go_to_guitars_category()
    instruments.go_to_electric_guitars()
    instruments.select_random_card()
    instruments.open_product_card()
    instruments.check_product_title()

def test_add_product_to_cart(instruments):
    instruments.open()
    instruments.confirm_region()
    instruments.close_cookies()
    instruments.open_catalog()
    instruments.go_to_guitars_category()
    instruments.go_to_electric_guitars()
    instruments.select_random_card()
    instruments.open_product_card()
    instruments.add_product_to_cart()
    instruments.check_cart_badge()

def test_view_shopping_cart(instruments):
    instruments.open()
    instruments.confirm_region()
    instruments.close_cookies()
    instruments.open_catalog()
    instruments.go_to_guitars_category()
    instruments.go_to_electric_guitars()
    instruments.select_random_card()
    instruments.open_product_card()
    instruments.add_product_to_cart()
    instruments.open_cart()
    instruments.check_product_in_cart()

def test_delete_product_from_cart(instruments):
    instruments.open()
    instruments.confirm_region()
    instruments.close_cookies()
    instruments.open_catalog()
    instruments.go_to_guitars_category()
    instruments.go_to_electric_guitars()
    instruments.select_random_card()
    instruments.open_product_card()
    instruments.add_product_to_cart()
    instruments.open_cart()
    instruments.delete_product_from_cart()
    instruments.check_empty_cart()

def test_add_wishlist(instruments):
    instruments.open()
    instruments.confirm_region()
    instruments.close_cookies()
    instruments.open_catalog()
    instruments.go_to_guitars_category()
    instruments.go_to_electric_guitars()
    instruments.select_random_card()
    instruments.open_product_card()
    instruments.add_product_to_wishlist()
    instruments.open_wishlist()
    instruments.check_adding_to_wishlist()