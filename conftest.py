import os

import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from src.flows.login_flow import LoginFlow
from src.flows.product_flow import ProductFlow
from src.flows.search_result_flow import SearchResultFlow
from src.pages.cart_page import CartPage
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage

load_dotenv()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser_instance = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser_instance
        browser_instance.close()


@pytest.fixture
def page(browser, request):
    video_dir = os.path.join(os.getcwd(), "videos")
    os.makedirs(video_dir, exist_ok=True)

    context = browser.new_context(
        no_viewport=True,
        record_video_dir=video_dir,
        record_video_size={"width": 1920, "height": 1080}
    )
    page_instance = context.new_page()

    yield page_instance

    if request.node.rep_call.failed:
        screenshot = page_instance.screenshot()
        allure.attach(
            screenshot,
            name="Screenshot on Failure",
            attachment_type=allure.attachment_type.PNG
        )

        video_path = None
        if page_instance.video:
            video_path = page_instance.video.path()

        page_instance.close()
        context.close()

        if video_path and os.path.exists(video_path):
            allure.attach.file(
                video_path,
                name="Video on Failure",
                attachment_type=allure.attachment_type.WEBM
            )
    else:
        video_path = None
        if page_instance.video:
            video_path = page_instance.video.path()

        page_instance.close()
        context.close()

        if video_path and os.path.exists(video_path):
            os.remove(video_path)


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def product_flow(page):
    return ProductFlow(page)


@pytest.fixture
def search_result_flow(page):
    return SearchResultFlow(page)


@pytest.fixture
def login_flow(page):
    return LoginFlow(page)
