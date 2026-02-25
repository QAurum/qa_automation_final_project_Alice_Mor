from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
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
            f"Неверный домен: {current_url}"
        
        # Проверяем путь
        assert "/accounts/login/" in current_url, \
            f"Это не страница логина: {current_url}"
        
        # Можно проверить протокол (https) - все-равно происходит перенаправление с http на https
        assert current_url.startswith("https"), \
            "Сайт должен использовать защищенное соединение"
        
        # Проверка на наличие 'login' в URL
        current_url = self.browser.current_url
        assert "login" in current_url, "'Login' not in this URL"

    def should_be_login_form(self):
        # Проверка что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Проверка что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Gegister form is present"
