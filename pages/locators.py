from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class MainPageOnlineShop():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    NAMEBOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    NAMEBOOKINBASKET = (By.CSS_SELECTOR, "div > div.alert:nth-child(1) > div.alertinner > strong")
    PRICEINBASKET = (By.CSS_SELECTOR, "div > div.alert:nth-child(3) > div.alertinner > p > strong")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div > div.alert:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group > a.btn")
    BASKET_ITEMS = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")
