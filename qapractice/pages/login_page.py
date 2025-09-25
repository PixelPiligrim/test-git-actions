from qapractice.pages.base_page import BasePage
from selenium.webdriver.common.by import By

input_email_selector = (By.ID, 'email')
input_password_selector = (By.ID, 'password')
button_submit_selector = (By.ID, 'submitLoginBtn')

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        
    def open(self):
        self.browser.get("https://qa-practice.netlify.app/auth_ecommerce")
        
    def is_loaded(self):
        return self.is_element_present(input_email_selector)
        
    def close(self):
        self.browser.quit()
        
    def input_email(self):
        return self.find(input_email_selector)
    
    def input_email_placeholder(self):
        return self.input_email().get_attribute("placeholder")
    
    def input_email_is_displayed(self):
        return self.input_email().is_displayed()
    
    def input_password(self):
        return self.find(input_password_selector)
    
    def input_password_placeholder(self):
        return self.input_password().get_attribute("placeholder")
    
    def input_password_is_displayed(self):
        return self.input_password().is_displayed()
    
    def button_submit(self):
        return self.find(button_submit_selector)
    
    def button_submit_is_displayed(self):
        return self.button_submit().is_displayed()
    
    def button_submit_text(self):
        return self.button_submit().text 
    
    def login(self, user):
        self.type_text(input_email_selector, user.email)
        self.type_text(input_password_selector, user.password)
        self.click_button(button_submit_selector)
        from .store_page import StorePage
        return StorePage(self.browser)    