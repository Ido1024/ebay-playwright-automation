import logging
import os
import time
from venv import logger

from playwright.sync_api import Page, Locator, TimeoutError

from src.utils.date_utils import DateUtils

logging.basicConfig(level=logging.INFO)


class BasePage:
    def __init__(self, page: Page):
        self.loading_spinner = page.get_by_role("img", name="loading")
        self.page = page

    def take_screenshot(self, name: str):
        folder = "screenshots"
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = os.path.join(folder, f"{name}_{DateUtils.get_current_date_time()}.png")
        self.page.screenshot(path=file_path)
        logger.info(f"[LOG] Screenshot  saved successfully at: {file_path}")

    def navigate(self, url: str):
        self.page.goto(url)

    def type_text(self, locator: Locator, text: str):
        locator.fill(text)

    def click_element(self, locator: Locator):
        locator.click()

    def press_key(self, locator: Locator, key: str):
        locator.press(key)

    def scroll_to(self, locator: Locator):
        locator.scroll_into_view_if_needed()

    def type_text_with_retries(self, locator: Locator, text: str, retries: int = 10, wait_time_ms: int = 200) -> bool:
        attempt = 0
        while attempt < retries:
            try:
                locator.fill(text)
                time.sleep(wait_time_ms / 1000.0)
                if locator.input_value() != "":
                    return True
            except Exception:
                pass

            attempt += 1

        raise TimeoutError(f"Timed out: Could not fill text '{text}' into the element after {retries} attempts")

    def is_element_present(self, locator: Locator, retries: int = 10, wait_time_ms: int = 100) -> bool:
        attempt = 0
        while attempt < retries:
            try:
                locator.wait_for(state="visible", timeout=wait_time_ms)
                return True
            except TimeoutError:

                attempt += 1

        return False

    def is_element_hidden(self, locator: Locator, retries: int = 10, wait_time_ms: int = 100) -> bool:
        attempt = 0
        while attempt < retries:
            try:
                locator.wait_for(state="hidden", timeout=wait_time_ms)
                return True
            except TimeoutError:

                attempt += 1

        return False

    def wait_for_spinner_to_disappear(self):
        self.is_element_hidden(self.loading_spinner, retries=20, wait_time_ms=100)
