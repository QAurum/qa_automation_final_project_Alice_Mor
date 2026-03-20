from pages.base_page import BasePage
from pages.locators import BasePageLocators, BasketPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import math
# базовая страница, от которой будут унаследованы все остальные классы. В ней  описаны вспомогательные методы для работы с драйвером

class BasketPage(BasePage):

# Методы-проверки (assertions) — с assert

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "❌ Find items in basket. WHY?"

    def should_see_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
        "❌ Messege about empty basket not found"
