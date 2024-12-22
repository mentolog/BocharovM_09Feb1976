import pytest
from main_page_api import CartAPI

COOKIES = {
    "CID": "9eb130fc0a3c4f5732a17c6d501d1d",
    "PHPSESSID": "b4kg7a5h74t1jim67olt9hfqn2",
    "_userGUID": "0m4mvmby:RK5ZRPuKfVNJAjBE970j1FG5uvig8",
    "site_countryID": "247"
}
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "; ".join([f"{key}={value}" for key, value in COOKIES.items()])
}

def test_add_product_to_cart_api():
    api = CartAPI(COOKIES, HEADERS)
    response = api.add_product_to_cart(product_id=3052, quantity=1)
    assert response.status_code == 200
    assert "error" not in response.text

def test_update_product_quantity_in_cart_api():
    api = CartAPI(COOKIES, HEADERS)
    response = api.update_product_quantity(product_id=3052, quantity=5)
    assert response.status_code == 200
    assert "error" not in response.text
