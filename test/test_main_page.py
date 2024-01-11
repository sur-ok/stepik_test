import pytest
from basepage import BasePage

from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators, BasketPageLocators
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        login_page = page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_quest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.click_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_empty_book(*BasketPageLocators.BASKET_SUMMARY)
    basket_page.check_empty_basket(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
