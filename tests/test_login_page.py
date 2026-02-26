# Описывает ЧТО проверяем (сценарии)
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time
import random

    # Вспомогательные функции для регистрации
def generate_unique_email():
    timestamp = int(time.time())
    return f"test_user_{timestamp}@example.com"

def generate_password(length=10):
    letters = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return ''.join(random.choice(letters) for _ in range(length))
    
    
#-------------------------------------------------------------------------------------------------
    
    
    # потом тут допишу проверку url при переоде чтобы сразу начинать тесты с url 'login'
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_url()  # проверка соответствия URL
    # page.should_be_login_link()  # проверяем, что ссылка есть

    # Проверка что мы на странице логина
def test_guest_have_true_login_page(browser, request):
    language = request.config.getoption("language")  # язык из CMD передаем а метод
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page(language)

    # Проверка правильности URL-а
def test_guest_have_true_login_url(browser, request):
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url(language)
    
    # Проверка что есть форма логина
def test_guest_should_see_login_form(browser):
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
    # Проверка что есть форма регистрации
def test_guest_should_see_register_form(browser):
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
#-------------------------------------------------------------------------------------------------
    

# УСПЕШНАЯ АВТОРИЗАЦИЯ
def test_guest_can_login_with_valid_data(browser, request):
    language = request.config.getoption("language")
    link = f"https://selenium1py.pythonanywhere.com/{language}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.login_user("test_alise_mor@email.com", "password123password123")
    page.should_be_authorized_user()
# 🔴 Ожидаемая ошибка: AttributeError: 'LoginPage' object has no attribute 'login_user'

# НЕУСПЕШНАЯ АВТОРИЗАЦИЯ
def test_guest_can_not_login_with_invalid_data(browser, request):
    language = request.config.getoption("language")
    link = f"https://selenium1py.pythonanywhere.com/{language}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.login_user("test@email", "password123")
    page.should_be_error_message()
    
    
#-------------------------------------------------------------------------------------------------

    # РЕГИСТРАЦИЯ
def test_guest_can_register(browser,request):
    language = request.config.getoption("language")
    link = f"https://selenium1py.pythonanywhere.com/{language}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    
    page.should_be_login_form()
    
    # Генерируем уникальные данные
    email = generate_unique_email()
    password = generate_password()
    # Логирование зареганного пользователя чтобы проверять под кем проходил тест
    print(f"\n 👏 Регистрирация пользователя: {email} / {password}")
    
    page.register_user(email, password, password)
    page.should_be_authorized_user()
