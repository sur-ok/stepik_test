import pytest
import faker

from test.pages.basket_page import BasketPage
from test.pages.locators import ProductPageLocators, BasketPageLocators
from test.pages.login_page import LoginPage
from test.pages.product_page import ProductPage


@pytest.mark.user
class TestUserAddBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    @pytest.mark.need_review
    def setup(self, browser):
        f = faker.Faker()
        email = f.email()
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = LoginPage(browser, link)
        page.open()
        page.registered_new_user(email, "juTpQW5FyZ75Gie")
        page.should_be_authorized_user()

    pytest.mark.xfail()

    @pytest.mark.need_review
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        # page.solve_quiz_and_get_code()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    @pytest.mark.xfail()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_product()
        # page.solve_quiz_and_get_code()
        assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_book_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.check_book()


@pytest.mark.need_review
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    # page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    # page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.click_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_empty_book(*BasketPageLocators.BASKET_SUMMARY)
    basket_page.check_empty_basket(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
