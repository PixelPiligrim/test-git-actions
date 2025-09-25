from qapractice.pages.login_page import LoginPage

def test_input_email_exists(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.input_email_is_displayed()
    login_page.close()
    
def test_input_email_has_correct_placeholder(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.input_email_placeholder() == "Enter email - insert admin@admin.com"
    login_page.close()
    
def test_input_password_exists(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.input_password_is_displayed()
    login_page.close()
    
def test_input_password_has_correct_placeholder(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.input_password_placeholder() == "Enter Password - insert admin123"
    login_page.close()
    
def test_button_submit_exists(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.button_submit_is_displayed()
    login_page.close()
    
def test_button_submit_has_correct_text(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.button_submit_text() == "Submit"
    login_page.close()
    
def test_login_successful(browser, valid_user):
    login_page = LoginPage(browser)
    login_page.open()
    store_page = login_page.login(valid_user)
    assert store_page.is_loaded
    login_page.close()