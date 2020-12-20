import faker
import time
from base_page import BasePage
from locators import LoginPageLocators
class LoginPage(BasePage):
    def register_new_user(self,email,password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
