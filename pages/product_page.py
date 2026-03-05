from .base_page import BasePage
from .locators import CataloguePageLocators
import time

class ProductPage(BasePage):   # наследуем от BasePage вычисления и промт
    
    
    def add_to_basket(self): # self.method() — ищет метод в текущем классе
        add_button = self.browser.find_element(*CataloguePageLocators.ADD_TO_BASKET)
        add_button.click()
        
    def solve_quiz_and_get_code(self):
        super().solve_quiz_and_get_code() # super().method() — ищет метод в родительском классе (BasePage)
    
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*CataloguePageLocators.ADD_TO_BASKET), \
        "❌ Button 'ADD TO BASKET' not found"

    def get_product_name(self):
        return self.browser.find_element(*CataloguePageLocators.PRODUCT_NAME).text # так получаем его текст
        
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
        #print(f"\n📨 ПОЛНОЕ СООБЩЕНИЕ: '{full_message}'")
        assert self.is_element_present(*CataloguePageLocators.SUCCESS_MESSAGE), \
        f"❌ Succes message not found"
        
    def should_be_basket_price_message(self):
        message_price = self.browser.find_element(*CataloguePageLocators.BASKET_PRICE_MESSAGE)
        full_message_price = message_price.text
        #print(f"\n📨 ПОЛНОЕ СООБЩЕНИЕ ЦЕНЫ: '{message_price.text}'")
        assert self.is_element_present(*CataloguePageLocators.BASKET_PRICE_MESSAGE), \
        f"❌ Basket price message not found"
    



    def should_be_correct_product_name_in_message(self, expected_name):
        name_element = self.browser.find_element(*CataloguePageLocators.SUCCESS_MESSAGE)
        actual_name = name_element.text
        
        assert actual_name == expected_name, \
            f"❌ Название в сообщении '{actual_name}' не совпадает с ожидаемым '{expected_name}'"


    def should_be_correct_price_in_basket_message(self, expected_price):
        price_element = self.browser.find_element(*CataloguePageLocators.BASKET_PRICE_MESSAGE)
        actual_price = price_element.text
        
        assert actual_price == expected_price, \
            f"❌ Цена в сообщении '{actual_price}' не совпадает с ожидаемой '{expected_price}'"
