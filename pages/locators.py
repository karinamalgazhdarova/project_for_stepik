from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIT_SUBMIT = (By.CSS_SELECTOR, "#login_submit")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "#registration_submit")
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"