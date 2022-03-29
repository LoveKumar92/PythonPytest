from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage


class ConfirmPage(BasePage):

    """By locator"""
    PRODUCT_HEADING = (By.CSS_SELECTOR, "div.media h4 a")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")
    COUNTRY_TEXT_BOX = (By.ID, "country")
    SUGGESTED_COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "div.suggestions li a")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "[value='Purchase']")
    SUCCESS_TEXT = (By.CSS_SELECTOR, "div.alert-success")

    """Constructor of class"""
    def __init__(self, driver):
        super().__init__(self.driver)

    """Page Actions for Confirm Page"""

    """this is used to get product name form cart"""
    def get_product_name(self):
        return self.get_element_text(self.PRODUCT_HEADING)

    """this is used to verify product name displayed in cart"""
    def is_product_name_displayed(self):
        return self.is_displayed(self.PRODUCT_HEADING)

    """this is used to click checkout button of cart"""
    def click_checkout_button(self):
        self.do_click(self.CHECKOUT_BUTTON)

    """this is used to enter country name"""
    def enter_country_name(self):
        self.do_send_keys(self.COUNTRY_TEXT_BOX)

    """this is used to select country name from suggestion dropdown"""
    def select_country_from_suggestion(self):
        self.do_click(self.SUGGESTED_COUNTRY_DROPDOWN)

    """this is used to click checkbox of purchase button of cart"""
    def click_purchase_button_checkbox(self):
        self.driver.execute_script("document.getElementById('checkbox2').click();")

    """this is used to click purchase button of cart"""
    def click_purchase_button(self):
        self.do_click(*ConfirmPage.PURCHASE_BUTTON)

    """this is used to verify success text displayed after placing order"""
    def is_success_text_displayed(self):
        return self.is_displayed(self.SUCCESS_TEXT)

    """this is used to get success text after placing order"""
    def get_success_text(self):
        return self.get_element_text(self.SUCCESS_TEXT)
