from playwright.sync_api import Page

from src.pages.base_page import BasePage
from src.utils.string_utils import StringUtils


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.string_utils = StringUtils()

        self._subtotal_locator = page.locator('[data-test-id="SUBTOTAL"]')
        self._remove_item = page.locator("[data-test-id='cart-remove-item']")

    def get_subtotal_number(self):
        self.is_element_present(self._subtotal_locator)
        raw_text = self._subtotal_locator.inner_text()
        return self.string_utils.extract_float_number(raw_text)

    def remove_all_items_from_cart(self):
        while self._remove_item.count() > 0:
            current_count = self._remove_item.count()
            first_btn = self._remove_item.first
            self.is_element_present(first_btn)
            self.scroll_to(first_btn)
            self.click_element(first_btn)
            last_item_locator = self._remove_item.nth(current_count - 1)
            last_item_locator.wait_for(state="hidden", timeout=5000)

    def is_cart_empty(self):
        return self._remove_item.count() == 0
