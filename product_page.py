from base_page import BasePage
from selenium.webdriver.common.by import By
from locators import ProductPageLocators


class ProductPage (BasePage):
    def btn_add(self):
       btn_add = self.browser.find_element(*ProductPageLocators.BTN_ADD)
       btn_add.click()


    def comperser(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        price_text = price.text
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        name_of_book_text = name_of_book.text
        alert_name = self.browser.find_element(*ProductPageLocators.NAME_FROM_BASKET)
        alert_name_text=alert_name.text
        alert_price =self.browser.find_element(*ProductPageLocators.PRICE_FROM_BASKET)
        alert_price_text=alert_price.text
        assert name_of_book_text == alert_name_text, f"wrong {name_of_book_text},{alert_name_text}"
        assert price_text == alert_price_text, f"wrong {price_text},{alert_price_text}"


    def should_not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BTN_ADD),'Its ok'


