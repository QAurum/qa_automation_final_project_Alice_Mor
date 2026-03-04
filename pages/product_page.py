from .base_page import BasePage
from .locators import CataloguePageLocators

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
        
        
    # ========== MESSEGE ==========
    
    def should_be_success_messege(self):
        assert self.is_element_present(*CataloguePageLocators.SUCCESS_MESSAGE), \
        f"❌ Succes message not found"
        
    def should_be_basket_price_messege(self):
        assert self.is_element_present(*CataloguePageLocators.BASKET_PRICE_MESSAGE), \
        f"❌ Basket price messege not found"
    
    def should_be_correct_product_name_in_messege(self, excepted_name):
        messege_text = self.browser.find_element(*CataloguePageLocators.SUCCESS_MESSAGE).text
        assert excepted_name in messege_text, \
        f"❌ Messege '{messege_text}' hasn't name '{excepted_name}'"
    
    def should_be_correct_product_price_in_messege(self, excepted_price):
        price_text = self.browser.find_element(*CataloguePageLocators.BASKET_PRICE_MESSAGE).text
        assert excepted_price in price_text, \
        f"❌ Messege '{price_text}' hasn't '{excepted_price}'"
    
