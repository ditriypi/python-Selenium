from selenium.webdriver.common.by import By


class ProductPageLocators():
    BTN_ADD = (By.CSS_SELECTOR,"button.btn-add-to-basket")
    NAME_OF_BOOK =(By.CSS_SELECTOR,'.product_main>h1')
    PRICE_OF_BOOK= (By.CSS_SELECTOR,'p.price_color')
    NAME_FROM_BASKET= (By.CSS_SELECTOR,'div.alertinner strong')
    PRICE_FROM_BASKET = (By.CSS_SELECTOR,'div.alertinner p strong')
    BASKET_BTN = (By.CSS_SELECTOR,'span.btn-group>a.btn.btn-default')
    BASKET_IS_EMPTY = (By.ID,'content_inner')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,'nth-child(1)')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class  LoginPageLocators():
    EMAIL_FORM = (By.ID,"id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR,".form-group #id_registration-password1")
    CONFIRM_PASSWORD_FORM = (By.CSS_SELECTOR,'.form-group #id_registration-password2')
    REGISTER_BTN = (By.CSS_SELECTOR,"form#register_form>button.btn")




class MainPageLocators():
    MAIN_LINK = (By.ID,"login_link")
