import time

from pom.home_page_elements import Homepage
from playwright.sync_api import Playwright, sync_playwright
import pytest


@pytest.mark.regression
def test_navigate(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})

    page = context.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="networkidle")
    time.sleep(2)

    assert page.is_visible(Homepage.logo)

    context.close()
    browser.close()


@pytest.mark.smoke
def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})

    page = context.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="networkidle")
    page.fill(Homepage.user_name_input, "standard_user")
    page.fill(Homepage.pass_word_input, "secret_sauce")
    page.click(Homepage.log_in_submit)

    assert page.is_visible(Homepage.cart)

    context.close()
    browser.close()


@pytest.mark.skip(reason="not ready")
def test_login_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})

    page = context.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="networkidle")
    page.fill(Homepage.user_name_input, "standard_user")
    page.fill(Homepage.pass_word_input, "secret_sauce")
    page.click(Homepage.log_in_submit)

    assert page.is_visible(Homepage.cart)

    context.close()
    browser.close()


@pytest.mark.regression
def test_navigate(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})

    page = context.new_page()
    page.goto("https://www.saucedemo.com/", wait_until="networkidle")
    time.sleep(2)

    assert page.is_visible(Homepage.logo)

    context.close()
    browser.close()
