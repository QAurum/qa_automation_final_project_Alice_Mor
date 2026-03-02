from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    url_selenium1 = "http://selenium1py.pythonanywhere.com"
    target_link = "/ru/password-reset/"

    LOGIN_LINK = "'http://selenium1py.pythonanywhere.com/{language}/accounts/login/"
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
    WELCOME_MESSEGE_ICON = (By.CSS_SELECTOR, ".alertinner.wicon") #Спасибо за регистрацию! icon-ok-sign
