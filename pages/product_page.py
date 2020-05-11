from .base_page import BasePage
from .locators import MainPageOnlineShop
from selenium import webdriver

class ProductPage(BasePage):
    def add_to_basket(self):
        add_basket = self.browser.find_element(*MainPageOnlineShop.BUTTON_BASKET)
        add_basket.click()

    def should_be_add_basket(self):
        assert (self.browser.find_element(*MainPageOnlineShop.NAMEBOOK)).text==(self.browser.find_element(*MainPageOnlineShop.NAMEBOOKINBASKET)).text, "Text does not correspond " + self.browser.current_url
        assert (self.browser.find_element(*MainPageOnlineShop.PRICE)).text == (self.browser.find_element(*MainPageOnlineShop.PRICEINBASKET)).text, "Price does not correspond " + self.browser.current_url





