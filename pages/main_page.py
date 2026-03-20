from pages.base_page import BasePage
from pages.locators import MainPageLocators, BasketPageLocators, LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        
    def should_be_login_link(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK),\
        "❌ Login link is not presented"
