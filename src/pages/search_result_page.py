from src.pages.base_page import BasePage


class SearchResultPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self._min_price_input = page.get_by_role("textbox", name="Minimum Value in ILS")
        self._max_price_input = page.get_by_role("textbox", name="Maximum Value in ILS")
        self._submit_price_range_btn = page.get_by_role("button", name="Submit price range")
        self._filter_item = self.page.locator("li.srp-multi-aspect__item--applied")

    def scroll_to_price_range(self):
        self.is_element_present(self._submit_price_range_btn)
        self.scroll_to(self._submit_price_range_btn)

    def input_min_price(self, price: str):
        self.is_element_present(self._min_price_input)
        self.type_text_with_retries(self._min_price_input, price)

    def input_max_price(self, price: str):
        self.is_element_present(self._max_price_input)
        self.type_text_with_retries(self._max_price_input, price)

    def click_submit_price_range(self):
        self.click_element(self._submit_price_range_btn)

    def wait_for_price_filter_to_load(self):
        self._filter_item.first.wait_for(state="visible", timeout=10000)
