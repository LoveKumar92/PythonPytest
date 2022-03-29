from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage
from Actions.ConfirmPage import ConfirmPage


class CheckoutPage(BasePage):

    """By locator"""
    CARD_ADD_BUTTON = (By.XPATH, "//a[text()='Blackberry']/ancestor::div[@class='card h-100']//button")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "li.nav-item.active")

    """Constructor of class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Checkout Page"""

    """this is used to add product to cart"""
    def add_product_to_cart(self):
        self.do_click(self.CARD_ADD_BUTTON)

    """this is used to click checkout button to move to cart"""
    def click_checkout_button(self):
        self.do_click(self.CHECKOUT_BUTTON)
        return ConfirmPage(self.driver)

