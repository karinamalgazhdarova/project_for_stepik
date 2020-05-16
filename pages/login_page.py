from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
import  time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url==LoginPageLocators.LOGIN_URL, "Url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration submit is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRMPASSWORD_INPUT)
        input_confirm_password.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_button.click()
