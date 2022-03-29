
from Actions.HomePage import HomePage
from Tests.BaseTest import BaseTest


class Test_HomePage(BaseTest):

    def test_verify_correct_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_title("ProtoCommerce")
        assert title == "ProtoCommerce"

    def test_move_to_shop_item_page(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_shop_item_page()
        title = self.homePage.get_title("ProtoCommerce")
        assert title == "ProtoCommerce"

