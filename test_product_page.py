import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.base_page import BasePage


@pytest.mark.parametrize('promo_offer', [*range(0, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)])
def test_guest_can_add_product_to_basket(driver, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(driver, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.verify_name_of_a_book_is_similar()
    page.verify_price_of_item_is_similar()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(driver, link)
    page.open()
    page.add_product_to_basket()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(driver, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(driver, link)
    page.open()
    page.add_product_to_basket()
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
    page.should_not_be_success_message()

