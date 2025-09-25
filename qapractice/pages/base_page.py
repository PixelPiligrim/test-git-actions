from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        
    def find(self, args):
        return self.browser.find_element(*args)
    
    def find_multiple(self, args):
        return self.browser.find_elements(*args)
    
    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def type_text(self, locator, text):
        element = self.browser.find_element(*locator)
        element.send_keys(text)
        
    def click_button(self, locator):
        element = self.browser.find_element(*locator)
        element.click()