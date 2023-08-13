from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@value='Добавить в корзину']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[text()[contains(.,'добавлен')]]/strong")
    BOOK_NAME = (By.XPATH, "//div/h1")
    BASKET_ALERT_PRICE = (By.XPATH, "//p[text()[contains(.,'составляет')]]/strong")
    PRICE = (By.XPATH, "//article[@class='product_page']/div/div/p[@class='price_color']")
