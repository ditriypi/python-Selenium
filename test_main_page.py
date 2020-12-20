import pytest
from main_page import  MainPage
from locators import ProductPageLocators
@pytest.mark.login_guest
class TestLoginFromMainPage():
 def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
     url ="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
     page =  MainPage(browser,url)
     page.go_to_site()
     page.go_to_login_page()
     page.go_to_basket()
     page.empty_basket_check()


 def test_guest_should_see_login_link(self,browser):
     url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
     page = MainPage(browser,url)
     page.go_to_site()
     page.should_be_login_link()


@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    url ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = MainPage(browser,url)
    page.go_to_site()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)






