from .base_page import BasePage
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, driver):
        assert driver.current_url==MainPageLocators.LOGIN_LINK, "Url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIT_SUBMIT), "Login submit is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_SUBMIT), "Registration submit is not presented"