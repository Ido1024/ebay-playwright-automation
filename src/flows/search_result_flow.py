from src.pages.search_result_page import SearchResultPage


class SearchResultFlow:
    def __init__(self, page):
        self.page = page
        self.search_result_page = SearchResultPage(page)

    def set_price_range(self, min_val: str, max_val: str):
        self.search_result_page.scroll_to_price_range()
        self.search_result_page.input_min_price(min_val)
        self.search_result_page.input_max_price(max_val)
        self.search_result_page.click_submit_price_range()
        self.search_result_page.wait_for_price_filter_to_load()
