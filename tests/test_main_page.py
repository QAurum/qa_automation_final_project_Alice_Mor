from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser, request):
    language = request.config.getoption("language")  # язык из CMD
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес (создает объект page)
    page.open()
    page.go_to_login_page() # проверяем, что кнопка работает

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
