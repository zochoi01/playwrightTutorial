import pytest
from playwright.async_api import Playwright

@pytest.fixture
def set_up(page) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=200)
    # context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    #
    # page = context.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="networkidle")
    page.set_default_timeout(3000)

    yield page