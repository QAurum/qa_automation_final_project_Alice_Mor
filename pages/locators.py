from selenium.webdriver.common.by import By

class MainPageLocators():
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"

class LoginPageLocators():
    url_selenium1 = "http://selenium1py.pythonanywhere.com"
    target_link = "/ru/password-reset/"

    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/{language}/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    PASSWORD_RESET = (By.CSS_SELECTOR, "a[href*='/password-reset/']")
        
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    
    LOGIN_IN = (By.NAME, "login_submit")
    REGISTER_IN = (By.NAME, "registration_submit")

    
    ICON_USER = (By.CSS_SELECTOR, ".icon-user")
    ERROR_MASSEGE = (By.CSS_SELECTOR, ".alert.alert-danger")
    HINT = (By.CSS_SELECTOR, ".icon-exclamation-sign")
    WELCOME_MESSAGE_ICON = (By.CSS_SELECTOR, ".alertinner.wicon") #Спасибо за регистрацию! icon-ok-sign

class CataloguePageLocators():
    PRODUCT_PAGE = "/catalogue/the-shellcoders-handbook_209/?promo=newYear"  # параметр "?promo=newYear" чтобы получить проверочный код
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket") # кнопка добавления товара в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group")
    #BASKET_PAGE = "http://selenium1py.pythonanywhere.com/basket/"

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket_items")
