from playwright.sync_api import Page

from src.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._products_list = page.locator("ul.srp-results > li.s-card--horizontal")
        self._product_price = page.locator(".s-card__price")
        self._next_page_btn = page.get_by_role("link", name="Go to next search page")
        self._product_links = self._products_list.locator("a.s-card__link:has(div[role='heading'])")
        self._add_to_cart_btn = page.get_by_role("button", name="Add to cart")

        self._variation_groups = page.locator(
            "xpath=//div[@data-testid='x-msku-evo']/div[normalize-space(@class)='vim x-sku']")
        self._checkout_btn = page.locator("[data-testid='ux-call-to-action']").filter(has_text="Checkout")
        self._see_in_cart_btn = page.get_by_role("link", name="See in cart")

    def get_valid_options(self, index: int):
        return self._variation_groups.nth(index).locator(
            "xpath=.//div[contains(@class, 'listbox__option') and not(@aria-disabled='true') and not(contains(., 'Select'))]")

    def go_to_next_page(self):
        self.scroll_to(self._next_page_btn)
        self.click_element(self._next_page_btn)
        self.is_element_present(self._products_list.first)

    def get_product_links(self) -> list:
        return [link.get_attribute("href") for link in self._product_links.all()]

    def wait_for_products_to_load(self):
        self.is_element_present(self._products_list.first)

    def click_add_to_cart_btn(self):
        self.wait_for_spinner_to_disappear()
        self.click_element(self._add_to_cart_btn)

    def wait_add_to_cart_btn(self):
        self.is_element_present(self._add_to_cart_btn)
        self.scroll_to(self._add_to_cart_btn)

    def click_valid_option_by_index(self, index: int, option_index: int):
        valid_option = self.get_valid_options(index).nth(option_index)
        self.scroll_to(valid_option)
        self.click_element(valid_option)

    def get_variation_groups_count(self) -> int:
        self.is_element_present(self._variation_groups.first, 5)
        return self._variation_groups.count()

    def get_valid_options_count(self, index: int) -> int:
        return self.get_valid_options(index).count()

    def click_variation_group_by_index(self, index: int):
        self.scroll_to(self._variation_groups.nth(index))
        self.click_element(self._variation_groups.nth(index))

    def click_see_in_cart_btn(self):
        self.is_element_present(self._see_in_cart_btn)
        self.scroll_to(self._see_in_cart_btn)
        self.click_element(self._see_in_cart_btn)
