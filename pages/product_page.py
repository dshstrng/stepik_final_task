import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def verify_name_of_a_book_is_similar(self):
        book_name = self.driver.find_element(*ProductPageLocators.BOOK_NAME).text
        basket_alert_book_name = self.driver.find_element(*ProductPageLocators.ITEM_NAME_ALERT).text
        assert book_name == basket_alert_book_name, "The name of a book doesn't match the name in alert"
        print(f"Name of an item: {basket_alert_book_name}")

    def verify_price_of_item_is_similar(self):
        actual_item_price = self.driver.find_element(*ProductPageLocators.PRICE).text
        basket_alert_price = self.driver.find_element(*ProductPageLocators.BASKET_ALERT_PRICE).text
        assert actual_item_price == basket_alert_price, "The price of an item doesn't match the price in alert"
        print(f"Price of an item: {basket_alert_price}")
