import pytest
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

