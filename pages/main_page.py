from .base_page import BasePage    # Точка . означает "в этой же папке"
#from .main_page import MainPage
from .locators import MainPageLocators, BasketPageLocators, LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
# Заглушка т.к. класс пока пустой
    def __init__(self, *args, **kwargs): # __init__ вызывается при создании объекта
# Конструктор с ключевым словом super только вызывает конструктор класса предка 
# и передает ему все те аргументы, которые мы передали в конструктор MainPage
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK), "Login link not found"
        login_link.click()
        
    def should_be_login_link(self):
        assert self.browser.is_element_present(*LoginPageLocators.LOGIN_LINK),\
        "❌ Login link is not presented"
