from pages.base_page import BasePage
from pages.product_page import ProductPage
import pytest
import time

@pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])


def test_guest_can_add_product_to_basket(browser, link): # если прописать (browser, link) то будет искаться фикстура с link
    #link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    print(f"\n ТКСТ: {link}")
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес (создает объект page)
    page.open()
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
    
    
@pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()  # ждет 4 сек, что элемента НЕТ
    

@pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])
    
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
    
@pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message_disappeared()

    # Проверка перехода на страницу логична
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()