from playwright.sync_api import Page

from src.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._sign_in_btn = page.get_by_role("link", name="Sign in")
        self._search_input = page.get_by_role("combobox", name="Search for anything")

    def click_sign_in(self):
        self._sign_in_btn.wait_for(state="visible", timeout=10000)
        self.click_element(self._sign_in_btn)

    def perform_search(self, product_name: str):
        self.type_text_with_retries(self._search_input, product_name)
        self.press_key(self._search_input, "Enter")
