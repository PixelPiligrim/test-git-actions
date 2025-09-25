from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qapractice.models.user import User
import pytest

@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(4)
    return chrome_browser

@pytest.fixture()
def valid_user():
    return User(email="admin@admin.com",
                password="admin123")