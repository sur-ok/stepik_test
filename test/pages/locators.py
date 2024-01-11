from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_BUTTON = (By.XPATH, '//a[text()="View basket"]')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTERED_FORM = (By.CSS_SELECTOR, '#register_form')
    ENTER_OR_REGISTRY_BUTTON = (By.CSS_SELECTOR, '#login_link')
    EMAIL = (By.CSS_SELECTOR, '#register_form [name="registration-email"]')
    PASSWORD = (By.CSS_SELECTOR, '#register_form [name="registration-password1"]')
    REPEAT_PASSWORD = (By.CSS_SELECTOR, '#register_form [name="registration-password2"]')
    REGISTRATION_BUTTOM = (By.XPATH, '//button[text()="Register"]')


class ProductPageLocators:
    ADD_PRODUCT = (By.XPATH, '//button[text()="Добавить в корзину"]')
    TEXT_BOOK_ON_ALERT = (By.CSS_SELECTOR, '#messages>div:first-child >div >strong')
    TEXT_BOOK = (By.CSS_SELECTOR, '[class*="product_main"] > h1')
    PRICE_BOOK = (By.CSS_SELECTOR, 'p[class ="price_color"]')
    PRICE_BUSKET_ON_ALERT = (By.CSS_SELECTOR, '#messages>div:nth-child(3) >div>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, '.basket_summary')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
