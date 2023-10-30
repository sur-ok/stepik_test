import math

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class Testtest:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_testtest(self, browser):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input3.send_keys("aaa@aa.aa")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_unittest2(self, browser):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input3.send_keys("aaa@aa.aa")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    @pytest.mark.regression
    def test_exception1(self, browser):
        try:
            browser.get("http://selenium1py.pythonanywhere.com/")
            with pytest.raises(NoSuchElementException):
                browser.find_element(By.CSS_SELECTOR, "button.btn")
                pytest.fail("Не должно быть кнопки Отправить")
        finally:
            browser.quit()

    def test_exception2(self, browser):
        try:
            browser.get("http://selenium1py.pythonanywhere.com/")
            with pytest.raises(NoSuchElementException):
                browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
                pytest.fail("Не должно быть кнопки Отправить")
        finally:
            browser.quit()


@pytest.mark.lesson3_6
@pytest.mark.parametrize('count', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class test_lesson_3_6:
    def test_lesson_3_6(self, browser, count):
        link = f"https://stepik.org/lesson/{count}/step/1"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '[[placeholder="Напишите ваш ответ здесь..."]').click
