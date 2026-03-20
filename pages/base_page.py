from pages.locators import BasePageLocators, BasketPageLocators, LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import math
import time
    # базовая страница, от которой будут унаследованы все остальные классы. В ней  описаны вспомогательные методы для работы с драйвером

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)


    # Методы-действия (actions) — без assert

    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK) #LOGIN_LINK_INVALID для негативной проверки
        login_link.click()

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_link.click()


# Методы-проверки (assertions) — с assert

    def should_be_basket_button(self):
        assert self.is_element_present(*BasePageLocators.BASKET_BUTTON),\
        "❌ Basket button is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
        "❌ Login link is not presented"
        

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False  # элемента нет
        except (InvalidSelectorException):
            return False
        return True
        
        
        # ===== UNTIL NOT =====

    # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
            EC.presence_of_element_located((how, what))
            )
            return True
        except TimeoutException:
            return False
            
        
            # ===== UNTIL =====

    # Проверяет, что элемент НЕ появляется
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until( # RemoteWebDriver - создание нового вебдрайвера
                EC.presence_of_element_located((how, what))
            )
            
            return False  # элемент появился
        except TimeoutException:
                return True


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"✅ Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            return self.browser.find_element(alert.text)
            
        
    def solve_quiz_and_get_code_without_second_alert(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        try:
            alert.accept()
        except NoAlertPresentException:
            return self.browser.find_element(alert.text)
        

    def should_not_be_success_message(self, timeout=4):
        assert self.is_not_element_present(*CataloguePageLocators.SUCCESS_MESSAGE, timeout=timeout), \
            f"❌ Сообщение об успехе появилось"
