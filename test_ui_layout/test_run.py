from pom.home_page_elements import Homepage
import pytest


@pytest.mark.regression
def test_navigate(set_up) -> None:
    page = set_up

    assert page.is_visible(Homepage.logo)

@pytest.mark.smoke
def test_login(set_up) -> None:
    page = set_up
    page.fill(Homepage.user_name_input, "standard_user")
    page.fill(Homepage.pass_word_input, "secret_sauce")
    page.click(Homepage.log_in_submit)

    assert page.is_visible(Homepage.cart)


@pytest.mark.skip(reason="not ready")
def test_login_2(set_up) -> None:
    page = set_up
    page.fill(Homepage.user_name_input, "standard_user")
    page.fill(Homepage.pass_word_input, "secret_sauce")
    page.click(Homepage.log_in_submit)

    assert page.is_visible(Homepage.cart)


@pytest.mark.regression
def test_navigate(set_up) -> None:
    page = set_up

    assert page.is_visible(Homepage.logo)
