# Описывает ЧТО проверяем (сценарии)
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time
import random

# ============== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==============

    # Для регистрации
def generate_unique_email():
    timestamp = int(time.time())
    return f"test_user_{timestamp}@example.com"

def generate_password(length=10):
    letters = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return ''.join(random.choice(letters) for _ in range(length))
    
    # Проверка поддерживаемых языков
def get_actual_language(requested_lang):
    # Словарь основных соответствий: базовый язык -> реальная локаль на сайте
    language_map = {
        "en": "en-gb",
        "es": "es",
        "fr": "fr",
        "ru": "ru"
}
    return language_map.get(requested_lang, requested_lang) # 2 параметра: что ищем в словаре, и что вернулось если не нашли
    
#-------------------------------------------------------------------------

    # Проверка что мы на странице логина
def test_guest_have_true_login_page(browser, request):
    language = request.config.getoption("language")  # язык из CMD передаем в метод rfr --lenguage=en_gb или ru и т.д.
    actual_lang = get_actual_language(language)  # используем функцию замены языка
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    login_page = page.should_be_login_page(language)

    # Проверка правильности URL-а
def test_guest_have_true_login_url(browser, request):
    language = request.config.getoption("language")
    actual_lang = get_actual_language(language)
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
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()
    
#-------------------------------------------------------------------------

# УСПЕШНАЯ АВТОРИЗАЦИЯ
def test_guest_can_login_with_valid_data(browser, request):
    language = request.config.getoption("language")
    lang = get_actual_language(language)
    link = f"https://selenium1py.pythonanywhere.com/{lang}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.login_user("test_alise_mor@email.com", "password123password123")
    page.SHOULD_be_authorized_user()

# НЕУСПЕШНАЯ АВТОРИЗАЦИЯ
def test_guest_can_not_login_with_invalid_data(browser, request):
    language = request.config.getoption("language")
    lang = get_actual_language(language)
    link = f"https://selenium1py.pythonanywhere.com/{lang}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.login_user("test@email", "password123")
    page.should_NOT_be_authorized_user()
    
    
#-------------------------------------------------------------------------

    # УСПЕШНАЯ РЕГИСТРАЦИЯ
def test_guest_can_register(browser, request):
    language = request.config.getoption("language")
    lang = get_actual_language(language)
    link = f"https://selenium1py.pythonanywhere.com/{lang}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
    time.sleep(1)
    # Генерируем уникальные данные
    email = generate_unique_email()
    password = generate_password()
    # Логирование зареганного пользователя чтобы проверять под кем проходили тест
    print(f"\n 👏 Регистрирация пользователя: {email} / {password}")
    
    page.register_user(email, password, password)
    page.SHOULD_be_authorized_user()
    
    
    # РЕГИСТРАЦИЯ ПОД ДАННЫМИ ЗАРЕГИСТРИРОВАННОГО ПОЛЬЗОВАТЕЛЯ
def test_guest_already_register(browser, request):
    language = request.config.getoption("language")
    lang = get_actual_language(language)
    link = f"https://selenium1py.pythonanywhere.com/{lang}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
    time.sleep(1)
    page.register_user("test_alise_mor@email.com", "password123password123", "password123password123")
    page.should_be_authorized_user()
    
    # РЕГИСТРАЦИЯ С НЕВАЛИДНОЙ ПОЧТОЙ
def test_guest_cannot_register_invalid_email(browser, request):
    language = request.config.getoption("language")
    lang = get_actual_language(language)
    link = f"https://selenium1py.pythonanywhere.com/{lang}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
    page.register_user("test@email.", "password123password123", "password123password123")
    page.should_NOT_be_authorized_user()

    # РЕГИСТРАЦИЯ С НЕСОВПАДАЮЩИМИ ПАРОЛЯМИ
def test_guest_cannot_register_different_passwords(browser, request):
    language = request.config.getoption("language")
    lang = get_actual_language(language)
    link = f"https://selenium1py.pythonanywhere.com/{lang}/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
    page.register_user("test_alise_mor@email.com", "password123password123", "password444password444")
    page.should_NOT_be_authorized_user()
