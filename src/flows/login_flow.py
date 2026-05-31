
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage


class LoginFlow:
    def __init__(self, page):
        self.page = page
        self.product_page = ProductPage(page)
        self.home_page = HomePage(page)
        self.login_page = LoginPage(page)

    def login(self, username: str, password: str):
        self.home_page.click_sign_in()
        self.login_page.enter_email(username)
        self.login_page.click_continue_btn()
        self.login_page.enter_password(password)
        self.login_page.click_signin_btn()