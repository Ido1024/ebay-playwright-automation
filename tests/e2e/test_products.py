import os
from venv import logger

import allure

from src.utils.data_loader import load_test_data

MAX_PRODUCTS_TO_ADD = 5


@allure.feature("Product Search & Filter")
@allure.story(
    "Search, filter and add products to cart within budget")
def test_search_and_filter(
        page,
        home_page,
        login_flow,
        search_result_flow,
        product_flow,
        product_page,
        cart_page
):
    search_config = load_test_data("cases")
    base_url = os.getenv("BASE_URL")
    ebay_email = os.getenv("EMAIL")
    ebay_password = os.getenv("PASSWORD")

    product_name = search_config["product_name"]
    min_price = search_config["min_price"]
    max_price = search_config["max_price"]

    budget = MAX_PRODUCTS_TO_ADD * float(search_config["max_price"])

    with allure.step(f"Navigate to {base_url} and log in"):
        home_page.navigate(base_url)
        login_flow.login(ebay_email, ebay_password)

    with allure.step(f"Search for '{product_name}' and filter by price ({min_price} - {max_price})"):
        home_page.perform_search(product_name)
        search_result_flow.set_price_range(min_price, max_price)

    with allure.step(f"Collect and add {MAX_PRODUCTS_TO_ADD} items to cart"):
        product_links = product_flow.collect_product_links(limit=MAX_PRODUCTS_TO_ADD)
        for link in product_links:
            product_flow.add_item_to_cart(link)

    with allure.step("Verify cart subtotal does not exceed the budget"):
        product_page.click_see_in_cart_btn()
        subtotal = cart_page.get_subtotal_number()

        logger.info(f"[LOG] Subtotal: {subtotal}, Budget: {budget}")
        cart_page.take_screenshot("cart_subtotal")
        assert subtotal <= budget, (
            f"Subtotal {subtotal} exceeds the expected budget of {budget} "
            f"for {len(product_links)} items!"
        )

    with allure.step("Clean up: Remove all items from cart and verify it's empty"):
        cart_page.remove_all_items_from_cart()
        assert cart_page.is_cart_empty(), "Cart is not empty after removing all items!"
