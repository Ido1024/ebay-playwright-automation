from playwright.sync_api import Page

from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._email_input = self.page.get_by_test_id("userid")
        self._continue_btn = self.page.get_by_test_id("signin-continue-btn")
        self._password_input = self.page.get_by_test_id("pass")
        self._signin_btn = self.page.get_by_test_id("sgnBt")
        self._skip_btn = self.page.locator("#passkeys-cancel-btn")

    def enter_email(self, email: str):
        self._email_input.wait_for(state="visible", timeout=10000)
        self.type_text_with_retries(self._email_input, email)

    def click_continue_btn(self):
        self._continue_btn.click()

    def enter_password(self, password: str):
        self._password_input.wait_for(state="visible", timeout=30000)
        self.type_text_with_retries(self._password_input, password)

    def click_signin_btn(self):
        self._signin_btn.click()
