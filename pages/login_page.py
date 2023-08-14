from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        print("The login page is presented")

    def should_be_login_url(self):
        assert "login" in self.driver.current_url, "Login link is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.driver.find_element(*LoginPageLocators.SIGNUP_EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.driver.find_element(*LoginPageLocators.SIGNUP_PASSWORD_INPUT)
        password_input.send_keys(password)
        second_password_input = self.driver.find_element(*LoginPageLocators.SIGNUP_REPEAT_PASSWORD_INPUT)
        second_password_input.send_keys(password)
        signup_button = self.driver.find_element(*LoginPageLocators.SIGNUP_BUTTON)
        signup_button.click()
        assert self.is_element_present(*LoginPageLocators.SUCCESS_LOGIN_ALERT), "The registration failed"
