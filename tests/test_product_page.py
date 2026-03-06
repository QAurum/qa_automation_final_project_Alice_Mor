from pages.base_page import BasePage
from pages.product_page import ProductPage
import pytest
import time

@pytest.mark.parametrize('link', \
[\
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"#,
"""
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
"""
])

def test_guest_can_add_product_to_basket(browser, link):
    #link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    print(f"\n ТКСТ: {link}")
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес (создает объект page)
    page.open()
    should_not_be_success_message()  # ждет 4 сек, что элемента НЕТ
    page.should_be_add_to_basket_button() # кнопка добавления есть
    
    # Фиксируем название и цену для переисп. при проверке message
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    # Осн. задача
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    #page.take_screenshot(f"after_add_{link.split('=')[-1]}")
    page.should_be_success_message()
    page.should_be_basket_price_message()
    page.should_be_correct_product_name_in_message(product_name)
    page.should_be_correct_price_in_basket_message(product_price)
