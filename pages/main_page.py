from .base_page import BasePage    # Точка . означает "в этой же папке"
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"       #‼️ПЕРЕПРОВЕРИТЬ КАК РАБОТАЕТ и прописать для login_page?
        login_link.click()
        # При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес.
        return LoginPage(browser=self.browser, url=self.browser.current_url)
        
    def should_be_login_link(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
