from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        print("The item added to  basket")

    def verify_name_of_a_book_is_similar(self):
        book_name = self.driver.find_element(*ProductPageLocators.BOOK_NAME).text
        basket_alert_book_name = self.driver.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert book_name == basket_alert_book_name, "The name of a book doesn't match the name in alert"
        print(f"Name of an item: {basket_alert_book_name}")

    def verify_price_of_item_is_similar(self):
        actual_item_price = self.driver.find_element(*ProductPageLocators.PRICE).text
        basket_alert_price = self.driver.find_element(*ProductPageLocators.BASKET_ALERT_PRICE).text
        assert actual_item_price == basket_alert_price, "The price of an item doesn't match the price in alert"
        print(f"Price of an item: {basket_alert_price}")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
