from base_page import BasePage
from locators import ProductPageLocators
from locators import MainPageLocators
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


    def opened_main_page(self):
        main_page = self.browser.find_element(*MainPageLocators.MAIN_LINK)
        main_page.click()




