import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFormMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, driver):
        page = MainPage(driver, link)
        page.open()
        page.should_be_login_link()


def test_guest_should_see_login_url(driver):
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.is_basket_message_present()
    basket_page.is_basket_empty()
