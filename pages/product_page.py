from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        assert True

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def should_be_add_alert(self):
        assert self.is_element_present(*ProductPageLocators.ADD_ALERT_PRODUCT_NAME), "Add alert is not presented"

    def check_add_alert(self):
        add_alert = self.browser.find_element(*ProductPageLocators.ADD_ALERT_PRODUCT_NAME)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == add_alert.text, "Incorrect product name in add alert"

    def should_be_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ALERT), "Basket alert is not presented"

    def check_basket_alert(self):
        add_alert = self.browser.find_element(*ProductPageLocators.BASKET_ALERT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket = add_alert.text.split()[0]
        price = product_name.text.split()[0]
        assert basket == price, "Incorrect price in basket alert"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_ALERT_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_ALERT_PRODUCT_NAME), \
            "Success message is presented, but should not be"
