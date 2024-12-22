from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def scroll_down(self, pixels=400):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

class CategoryPage(BasePage):
    URL = "https://altaivita.ru/category/griby/"

    def open(self):
        with allure.step("Открытие страницы категории"):
            self.driver.get(self.URL)

    def close_cookie_popup(self):
        with allure.step("Закрытие всплывающего окна cookie"):
            popup = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fa-times-circle")))
            popup.click()

    def add_product_to_cart(self, product_id):
        with allure.step("Добавление товара в корзину"):
            self.scroll_down()
            product_card = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "product__item_ajax_zero_element"))
            )
            assert product_card.get_attribute("data-product-id") == product_id, "Неверный товар на странице"
            add_to_cart_button = product_card.find_element(By.CLASS_NAME, f"js-product__add_2_0_cat_preview_{product_id}")
            add_to_cart_button.click()

    def verify_add_to_cart_popup(self):
        with allure.step("Проверка уведомления о добавлении в корзину"):
            popup = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "action-notification_add_to_cart"))
            )
            assert popup.text == "Товар добавлен в корзину"

class CartPage(BasePage):
    URL = "https://altaivita.ru/cart/"

    def open(self):
        with allure.step("Открытие страницы корзины"):
            self.driver.get(self.URL)

    def remove_product_from_cart(self):
        with allure.step("Удаление товара из корзины"):
            cart_item = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "js-cart-item")))
            remove_button = cart_item.find_element(By.CLASS_NAME, "js-item-delete")
            remove_button.click()
            self.wait.until(EC.invisibility_of_element((By.CLASS_NAME, "cart__item")))

    def verify_cart_is_empty(self):
        with allure.step("Проверка, что корзина пуста"):
            empty_cart = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "js-total")))
            assert "0" in empty_cart.text
