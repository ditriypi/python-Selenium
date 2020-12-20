from product_page import ProductPage
from login_page import LoginPage
from base_page import   BasePage
import random
import pytest

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
   url ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
   page = ProductPage(browser,url)
   page.go_to_site()
   page.btn_add()
   page.solve_quiz_and_get_code()
   page.comperser()


def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,url)
    page.go_to_site()
    page.btn_add()
    page.should_se_success_massage()



@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,url)
    page.go_to_site()
    page.go_to_basket()
    page.empty_basket_check()

@pytest.mark.login
class TestLoginFromProductPage():
 @pytest.fixture(scope="function", autouse=True)
 def test_guest_should_see_login_link_on_product_page(self,browser):
     url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
     page = ProductPage(browser, url)
     page.go_to_site()
     page.should_be_login_link()

 @pytest.mark.need_review
 def test_guest_can_go_to_login_page_from_product_page(self,browser):
     url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
     page = ProductPage(browser,url)
     page.go_to_site()
     page.go_to_login_page()







class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setups(self,browser):
        url = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        chislo = random.randint(0, 1000)
        email = "email" + str(chislo * chislo) + "@email" + str(chislo) + ".com"
        password = "qwe123qwe" + str(chislo * chislo)
        page = LoginPage(browser,url)
        page.go_to_site()
        page.register_new_user(email,password)
        page =  BasePage(browser,url)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.go_to_site()
        page.should_be_authorized_user()
        page.btn_add()
        page.comperser()

    def test_user_should_see_login_link(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,url)
        page.go_to_site()
        page.should_be_authorized_user()






