from qapractice.pages.base_page import BasePage
from selenium.webdriver.common.by import By

title_store_page = (By.CLASS_NAME, "section-header")
button_checkout = (By.CLASS_NAME, "btn-purchase")
button_logout = (By.ID, "logout")
title_shop_item = (By.CLASS_NAME, "shop-item-title")
title_cart_item = (By.CLASS_NAME, "cart-item-title")

class StorePage(BasePage):       
    def __init__(self, browser):
        super().__init__(browser)
        
    def open(self, valid_user):
        from .login_page import LoginPage
        login_page = LoginPage(self.browser)
        login_page.open()
        return login_page.login(valid_user)
    
    def close(self):
        self.browser.quit()
    
    def is_loaded(self):
        return self.is_element_present(title_store_page)
    
    def logout(self):
        self.click_button(button_logout)
        from .login_page import LoginPage
        return LoginPage(self.browser)  
    
    def button_add_to_cart_phone(self, id):
        button_add_to_cart = (By.CSS_SELECTOR, "#prooood > section:nth-child(2) > div > div:nth-child(" + id + ") > div > button")
        self.click_button(button_add_to_cart)
        
    def check_phone(self, phone):
        elements = self.find_multiple(title_cart_item)
        for element in elements:
            print(element.text)
            if element.text == phone:
                return True