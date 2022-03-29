import time

from Actions.HomePage import HomePage
from Tests.BaseTest import BaseTest


class Test_Checkout(BaseTest):

    def test_add_product_to_cart(self):
        self.homePage = HomePage(self.driver)
        checkoutPage = self.homePage.move_to_shop_item_page()
        checkoutPage.add_product_to_cart()

    def test_checkout_from_shop(self):
        self.homePage = HomePage(self.driver)
        checkoutPage = self.homePage.move_to_shop_item_page()
        checkoutPage.click_checkout_button()
