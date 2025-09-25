from qapractice.pages.store_page import StorePage
import pytest

@pytest.mark.parametrize ("phone, id", [("Apple iPhone 12, 128GB, Black", "1"), ("Huawei Mate 20 Lite, 64GB, Black", "2"), ("Samsung Galaxy A32, 128GB, White", "3"),
                ("Apple iPhone 13, 128GB, Blue", "4"), ("Nokia 105, Black", "5")])   
def test_add_to_cart_phone(browser, valid_user, phone, id):
    print(phone)
    store_page = StorePage(browser)
    store_page.open(valid_user)
    store_page.button_add_to_cart_phone(id)
    assert store_page.check_phone(phone)
    store_page.close()  

def test_logout(browser, valid_user):
    store_page = StorePage(browser)
    store_page.open(valid_user)
    login_page = store_page.logout()
    assert login_page.is_loaded
    login_page.close()

def test_open(browser, valid_user):
    store_page = StorePage(browser)
    store_page.open(valid_user)
    assert store_page.is_loaded
    store_page.close()    