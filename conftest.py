import pytest
from selenium import webdriver

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
