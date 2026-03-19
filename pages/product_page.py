from .base_page import BasePage
from .locators import CataloguePageLocators
from selenium.webdriver.support.ui import WebDriverWait # Для явного ожидания
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*CataloguePageLocators.ADD_TO_BASKET)
        add_button.click()

    # super().method() — ищет метод в родительском классе (BasePage)
    def solve_quiz_and_get_code(self):
        super().solve_quiz_and_get_code()
        
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*CataloguePageLocators.ADD_TO_BASKET), \
        "❌ Button 'ADD TO BASKET' not found"

    def get_product_name(self):
        return self.browser.find_element(*CataloguePageLocators.PRODUCT_NAME).text
        
    def get_product_price(self):
        return self.browser.find_element(*CataloguePageLocators.PRODUCT_PRICE).text
        
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        self.browser.save_screenshot(filename)
        print(f"📸 Скриншот сохранен: {filename}")
        
    # ========== MESSAGE ==========
    
    def should_be_success_message(self):
        message_element = self.browser.find_element(*CataloguePageLocators.SUCCESS_MESSAGE)
        full_message = message_element.text
        assert self.is_element_present(*CataloguePageLocators.SUCCESS_MESSAGE), \
        f"❌ Succes message not found"

    def should_be_correct_name_in_basket_message(self, expected_name):
        name_element = self.browser.find_element(*CataloguePageLocators.SUCCESS_MESSAGE)
        actual_name = name_element.text
        
        assert actual_name == expected_name, \
            f"❌ Название в сообщении '{actual_name}' не совпадает с ожидаемым '{expected_name}'"


    def should_be_correct_price_in_basket_message(self, expected_price):
        price_element = self.browser.find_element(*CataloguePageLocators.BASKET_PRICE_MESSAGE)
        actual_price = price_element.text
        
        assert actual_price == expected_price, \
            f"❌ Цена в сообщении '{actual_price}' не совпадает с ожидаемой '{expected_price}'"
            
            
# ==================== НЕГАТИВНЫЕ ПРОВЕРКИ ====================

# Метод принимает параметры how, what, но внутри использует CataloguePageLocators
    def should_not_be_success_message(self, timeout=4):
        assert self.is_not_element_present(*CataloguePageLocators.SUCCESS_MESSAGE,
            timeout=timeout), "❌ Сообщение об успехе появилось"


    def should_be_success_message_disappeared(self, timeout=4):
        assert self.is_disappeared(
            *CataloguePageLocators.SUCCESS_MESSAGE, timeout=timeout # передача полученного значения параметра по имени в другой метод
        ), "❌ Сообщение об успехе не исчезло"
