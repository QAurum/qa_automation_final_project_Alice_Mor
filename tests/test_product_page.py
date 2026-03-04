from pages.base_page import BasePage
from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser, request):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес (создает объект page)
    page.open()
    #time.sleep(5)
    page.should_be_add_to_basket_button() # кнопка добавления есть
    
    # Фиксируем название и цену для переисп. при проверке messege
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    # Осн. задача
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_messege()
    page.should_be_basket_price_messege()
    page.should_be_correct_product_name_in_messege(product_name)
    page.should_be_correct_product_price_in_messege(product_price)
