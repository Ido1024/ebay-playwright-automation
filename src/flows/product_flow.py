# flows/product_flow.py
import random
from venv import logger

from src.pages.product_page import ProductPage


class ProductFlow:
    def __init__(self, page):
        self.page = page
        self.product_page = ProductPage(page)

    def collect_product_links(self, limit: int = 5) -> list:
        product_links = []
        while len(product_links) < limit:
            page_links = self.product_page.get_product_links()
            if not page_links:
                logger.info("No products found on the current page!")
                break

            for link in page_links:
                if link not in product_links:
                    product_links.append(link)
                if len(product_links) >= limit:
                    break

            if len(product_links) < limit:
                try:
                    if self.product_page._next_page_btn.is_visible():
                        self.product_page.go_to_next_page()
                        self.product_page.wait_for_products_to_load()
                    else:
                        break
                except:
                    break

        logger.info("product_links:")
        logger.info(product_links)
        return product_links[:limit]

    def add_item_to_cart(self, url: str):
        self.page.goto(url)
        self.product_page.wait_add_to_cart_btn()
        self.select_random_product_for_all_variations(self.product_page)
        self.product_page.click_add_to_cart_btn()
        self.product_page.take_screenshot("item_added")
        self.product_page.press_key(self.product_page._checkout_btn, "Escape")

    def select_random_product_for_all_variations(self, product_page: ProductPage):
        variation_groups_count = product_page.get_variation_groups_count()
        if variation_groups_count == 0:
            logger.info("[LOG] No variation groups found for this product.")
            return

        for index in range(variation_groups_count):
            product_page.click_variation_group_by_index(index)
            valid_options_count = product_page.get_valid_options_count(index)
            if valid_options_count > 0:
                random_option_index = random.randint(0, valid_options_count - 1)
                product_page.click_valid_option_by_index(index, random_option_index)
