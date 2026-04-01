import sys
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless') # позволяет запускать тесты в фоне без графического интерфейса. Это ускоряет парсинг сайтов и автоматизацию тестирования на серверах, экономя ресурсы.
# options.add_argument("--window-position=-2400,-2400") #для использования на версии хрома 29,30. Так как в селениуме открывается просто пустое окно, если хедлесс не указать без второй строчки

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="You need to choose language: es, fr, ru, etc.")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nНастройка нужного языка..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit exit...")
    browser.quit()
