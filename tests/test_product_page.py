from pages.base_page import BasePage
from pages.product_page import ProductPage

def test_guest_can_add_produat_in_basket(browser, request):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес (создает объект page)
    page.open()
    
    page.should_be_add_to_basket_button() # проверяем, что кнопка есть
    
    # Фиксируем название и цену для переисп. при проверке messege
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    # Осн. задача
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_name_in_messege(product_name)
    page.should_be_correct_product_price_in_messege(product_price)
