from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver import Remote as RemoteWebDriver
# базовая страница, от которой будут унаследованы все остальные классы. В ней  описаны вспомогательные методы для работы с драйвером

class BasePage():

# Первым делом добавим конструктор __init__ — метод, который вызывается, когда мы создаем объект. В него в качестве параметров мы передаем экземпляр драйвера и url адрес. Внутри конструктора сохраняем эти данные как аттрибуты нашего класса

    # self как this

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    # Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get(). Объявите ниже в том же классе:
    def open(self):
        self.browser.get(self.url)
        
    # В __init__ мы сохраняем данные (browser и url)
    # В open мы используем сохраненные данные через self

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (InvalidSelectorException):
            return False
        return True
