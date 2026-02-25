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
    
    # потом тут допишу проверку url при переоде чтобы сразу начинать тесты с url 'login'
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_url()  # проверка соответствия URL
    # page.should_be_login_link()  # проверяем, что ссылка есть


# нужно перенести в test_login_page.py
def test_guest_have_true_login_page(browser, request):
    language = request.config.getoption("language")  # язык из CMD передаем а метод
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page(language)

def test_guest_have_true_login_url(browser, request):
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url(language)
    
def test_guest_should_see_login_form(browser):
    #language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
def test_guest_should_see_register_form(browser):
    #language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
