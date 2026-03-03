# Описывает КАК работать со страницей (методы)
# ЗДЕСЬ мы говорим "найди поле, вставь данные, нажми кнопку"
from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators
from .login_page import LoginPage


class LoginPage(BasePage):
# Это композитный метод (метод, собирающий другие методы). Его задача — проверить, что мы действительно на странице логина
    def should_be_login_page(self, expected_language): # language принимаем из test_main_page как expected_language. Определяется этот парамтер просто по порядку, как передавался
        self.should_be_login_url(expected_language)
        self.should_be_login_form()
        self.should_be_register_form()

# Переход между страницами возвратом нужного Page Object:
    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) для инициализации страницы неявно через метод
        
#-------------------------------------------------------------------------------------------------

    #ПРОВЕРКИ
    def should_be_login_url(self, expected_language):
        # проверка на корректный url адрес
        current_url = self.browser.current_url # current_url это встроенное свойство Selenium, которое существует в WebDriver. Браузер запоминает адрес и его всегда можно получить по browser.current_url
        expected_url = f"https://selenium1py.pythonanywhere.com/{expected_language}/accounts/login/"

        # Т.к. сайт перенаправляет с просто en на британский en-gb то проверка вот такая:
        # Проверяем домен
        assert "selenium1py.pythonanywhere.com" in current_url, \
        f"❌ Wrong domain: {current_url}"
        
        # Проверяем путь
        assert "/accounts/login/" in current_url, \
        f"❌ It's not a login page: {current_url}. "
        
        # Можно проверить протокол (https) - все-равно происходит перенаправление с http на https
        assert current_url.startswith("https"), \
        "‼️ Site shouldn use HTTPS, not {current_url}"
        
        # Проверка на наличие 'login' в URL
        current_url = self.browser.current_url
        assert "login" in current_url, \
        "❌ 'Login' not in this URL"

    def should_be_login_form(self):
        # Проверка что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
        "❌ Login form is not presented"

    def should_be_register_form(self):
        # Проверка что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
        "✅ Register form is present"
        
#-------------------------------------------------------------------------------------------------

# Методы-действия (actions) — без assert
    def login_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_IN).click()
    
    def register_user(self, email, password1, password2):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD1).send_keys(password1)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD2).send_keys(password2)
        self.browser.find_element(*LoginPageLocators.REGISTER_IN).click()
        
    def user_fogot_password(self):
        self.browser.find_element(*LoginPageLocators.PASSWORD_RESET)
        
    
#-------------------------------------------------------------------------------------------------

# Методы-проверки (assertions) — с assert
    
    # Наличия сообщения об ошибке
    def should_be_error_message(self):
        assert self.browser.is_element_present(*LoginPageLocators.HINT), \
        "❌ Has't error messege"
    
    # Наличия иконки успеха
    def should_be_success_icon(self):
        assert self.browser.find_element(*LoginPageLocators.WELCOME_MESSEGE_ICON), \
        "❌ User wasn't authorized"
    
    # Залогинились
    def SHOULD_be_authorized_user(self): # Залогинились
        assert self.is_element_present(*LoginPageLocators.ICON_USER), \
        "❌ User wasn't Log In"

    # ======= ASSERT NOT =======
    def should_NOT_be_authorized_user(self): # НЕ залогинились
        assert not self.is_element_present(*LoginPageLocators.ICON_USER), \
        "‼️ User was authorized. WHY?"
    

