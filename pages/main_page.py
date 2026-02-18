from .base_page import BasePage    # Точка . означает "в этой же папке"
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self): # метод проверки should_be_(название элемента)
        assert self.browser.find_element(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
