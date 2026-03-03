from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
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
        # NoSuchElementException (когда элемента нет) не обрабатывался до тех пор пока его не прописали здесь:
        except (NoSuchElementException):  # ← правильное исключение!
            return False  # элемента нет
        except (InvalidSelectorException):
            return False
        return True


# После вычисления полученный код нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат
        def solve_quiz_and_get_code(self):
            prompt = self.browser.switch_to.alert
            prompt_text = prompt.text # Получаем текст
            x = prompt_text.split(" ")[2] # Разрезаем строку 'x = "12345"' по пробелам # ["x", "=", "12345"][2] = "12345"
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            prompt.send_keys(answer)
            prompt.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"✅ Verification code is {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("❌ Haven't secont alert")
