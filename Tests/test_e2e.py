# Best practice to wrap all test cases in one class
# Command line argument passing in pytest : https://docs.pytest.org/en/6.2.x/example/simple.html (All command line options in Pytest)
# To give Command line options in pytest use command "pytest -q --browser_name=chrome", where browser_name passing from command line
# To run parallel install pip install pytest-xdist
# And then command pytest -n 3 , Where -n 3 is number of thread



from Actions.CheckoutPage import CheckoutPage
from Actions.ConfirmPage import ConfirmPage
from Tests.BaseTest import BaseClass
from Actions.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutPage = CheckoutPage(self.driver)
        confirmPage = ConfirmPage(self.driver)
        driver = self.driver
        driver.implicitly_wait(3)
        homePage.shopItems().click()

        checkoutPage.selectProduct().click()
        checkoutPage.checkoutButton().click()

        ItemName = confirmPage.getItemNameText()
        assert confirmPage.getItemName().is_displayed()
        assert ItemName == "Blackberry"
        confirmPage.acceptButton().click()

        confirmPage.countryTextBox().send_keys("India")
        confirmPage.countryDropDownSuggestion().click()
        confirmPage.clickPurchaseCheckbox()
        confirmPage.purchaseButton().click()

        assert confirmPage.successButton().is_displayed()
        AlertText1 = confirmPage.successButton().text
        print(AlertText1)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in AlertText1
