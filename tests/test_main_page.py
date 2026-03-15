from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.main_page import MainPage
import pytest


#Бутут переписаны. В них сейчас нет необходимости

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()
    page.should_not_be_products_in_basket()
    page.should_see_message_basket_is_empty()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        main_link = self.browser.find_element(*MainPageLocators.MAIN_LINK)
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_link = self.browser.find_element(*MainPageLocators.MAIN_LINK),"Main link not found"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
