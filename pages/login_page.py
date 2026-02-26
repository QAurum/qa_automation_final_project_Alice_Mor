# Описывает КАК работать со страницей (методы)
# ЗДЕСЬ мы говорим "найди поле, вставь данные, нажми кнопку"
from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
# Это композитный метод (метод, собирающий другие методы). Его задача — проверить, что мы действительно на странице логина
    def should_be_login_page(self, expected_language): # language принимаем из test_main_page как expected_language. Определяется этот парамтер просто по порядку, как передавался
        self.should_be_login_url(expected_language)
        self.should_be_login_form()
        self.should_be_register_form()

    #ПРОВЕРКИ
    def should_be_login_url(self, expected_language):
        # проверка на корректный url адрес
        current_url = self.browser.current_url # current_url это встроенное свойство Selenium, которое существует в WebDriver. Браузер запоминает адрес и его всегда можно получить по browser.current_url
        expected_url = f"https://selenium1py.pythonanywhere.com/{expected_language}/accounts/login/"

        # Т.к. сайт перенаправляет с просто en на британский en-gb то проверка вот такая:
        # Проверяем домен
        assert "selenium1py.pythonanywhere.com" in current_url, \
        f"❌ Неверный домен: {current_url}"
        
        # Проверяем путь
        assert "/accounts/login/" in current_url, \
        f"❌ Это не страница логина: {current_url}"
        
        # Можно проверить протокол (https) - все-равно происходит перенаправление с http на https
        assert current_url.startswith("https"), \
        "‼️ Сайт должен использовать защищенное соединение"
        
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
        
    # Методы-действия (actions) — без assert
    def login_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_IN).click()
    
    def register_user(self, email, password1, password2):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD1).send_keys(password1)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD2).send_keys(password2)
        self.browser.find_element(*LoginPageLocators.LOGIN_IN).click()
        
    def user_fogot_password(self):
        self.browser.find_element(*LoginPageLocators.PASSWORD_RESET)
        
    
    
    # Методы-проверки (assertions) — с assert
    
    # Наличия сообщения об ошибке
    def should_be_error_message(self):
        self.browser.find_element(*LoginPageLocators.HINT)
    
    # Наличие конкретного текста в сообщениях об ошибках
#    def should_be_error_incorrect_email(self):
#        error_element = self.browser.find_element(By.CSS_SELECTOR, ".icon-exclamation-sign")
#        actual_error_text = error_element.text
#        assert "Введите корректный адрес электронной почты." in actual_error_text, f"Вместо нужной ошибки - '{actual_error_text}'"
    
    # Наличия иконки успеха
    def should_be_success_icon(self):
        self.browser.find_element(*LoginPageLocators.WELCOME_MESSEGE_ICON)
    
    def should_be_authorized_user(self): # Проверка, что залогинились
        assert self.is_element_present(*LoginPageLocators.ICON_USER), \
        "❌ User wasn't authorized"
    

