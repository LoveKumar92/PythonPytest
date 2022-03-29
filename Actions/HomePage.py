from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage
from Actions.CheckoutPage import CheckoutPage


class HomePage(BasePage):

    """By locator"""
    SHOP_BUTTON = (By.CSS_SELECTOR, "a[href*='shop']")

    """Constructor of class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Home Page"""

    """this is used to get the page title"""
    def get_page_title(self, title):
        return self.get_title(title)

    """this is used to click on shop items"""
    def move_to_shop_item_page(self):
        self.do_click(self.SHOP_BUTTON)
        return CheckoutPage(self.driver)

