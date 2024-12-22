from main_page_ui import CategoryPage, CartPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

def test_add_product_to_cart_ui():
    # Инициализация браузера
    driver = webdriver.Chrome(service=ChromeService())
    try:
        category_page = CategoryPage(driver)
        category_page.open()
        category_page.close_cookie_popup()
        category_page.add_product_to_cart(product_id="3052")
        category_page.verify_add_to_cart_popup()
    finally:
        driver.quit()

def test_remove_product_from_cart_ui():
    # Инициализация браузера
    driver = webdriver.Chrome(service=ChromeService())
    try:
        category_page = CategoryPage(driver)
        cart_page = CartPage(driver)

        category_page.open()
        category_page.close_cookie_popup()
        category_page.add_product_to_cart(product_id="3052")
        category_page.verify_add_to_cart_popup()

        cart_page.open()
        cart_page.remove_product_from_cart()
        cart_page.verify_cart_is_empty()
    finally:
        driver.quit()
