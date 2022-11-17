from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Incorrect basket url"

    def should_be_message_about_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST), "Basket is not empty"
