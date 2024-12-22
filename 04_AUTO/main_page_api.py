import requests
import allure

class CartAPI:
    BASE_URL = "https://altaivita.ru/engine/cart"

    def __init__(self, cookies, headers):
        self.cookies = cookies
        self.headers = headers

    @allure.step("Добавление товара в корзину")
    def add_product_to_cart(self, product_id, quantity):
        payload = {
            "product_id": product_id,
            "LANG_key": "ru",
            "S_wh": "1",
            "S_CID": self.cookies["CID"],
            "S_cur_code": "rub",
            "S_koef": "1",
            "quantity": quantity,
            "S_hint_code": "",
            "S_customerID": ""
        }
        response = requests.post(f"{self.BASE_URL}/add_products_to_cart_from_preview.php", 
                                 headers=self.headers, data=payload)
        return response

    @allure.step("Изменение количества товара в корзине")
    def update_product_quantity(self, product_id, quantity):
        return self.add_product_to_cart(product_id, quantity)
