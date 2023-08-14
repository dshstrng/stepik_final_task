from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    SIGNUP_EMAIL_INPUT = (By.XPATH, "//input[@name='registration-email']")
    SIGNUP_PASSWORD_INPUT = (By.XPATH, "//input[@name='registration-password1']")
    SIGNUP_REPEAT_PASSWORD_INPUT = (By.XPATH, "//input[@name='registration-password2']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    SUCCESS_LOGIN_ALERT = (By.XPATH, "//div[1]/div[@class='alertinner wicon']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@value='Добавить в корзину']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[text()[contains(.,'добавлен')]]/strong")
    BOOK_NAME = (By.XPATH, "//div/h1")
    BASKET_ALERT_PRICE = (By.XPATH, "//p[text()[contains(.,'составляет')]]/strong")
    PRICE = (By.XPATH, "//article[@class='product_page']/div/div/p[@class='price_color']")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.XPATH, "//div[@id='content_inner']/p")
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")
