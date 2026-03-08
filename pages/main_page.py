from .base_page import BasePage    # Точка . означает "в этой же папке"
from .main_page import MainPage
from locators import MainPageLocators, BasketPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
# Заглушка т.к. класс пока пустой
    def __init__(self, *args, **kwargs): # __init__ вызывается при создании объекта
# Конструктор с ключевым словом super только вызывает конструктор класса предка 
# и передает ему все те аргументы, которые мы передали в конструктор MainPage
        super(MainPage, self).__init__(*args, **kwargs)