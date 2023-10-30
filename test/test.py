import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.lesson3_6
@pytest.mark.parametrize('count', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class Test_lesson_3_6:
    def test_lesson_3_6(self, browser, count):
        link = f"https://stepik.org/lesson/{count}/step/1"
        browser.get(link)
        #WebDriverWait(browser, 300).until(EC.visibility_of_element_located(browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))
        WebDriverWait(browser, 300).until(EC.element_to_be_clickable((By.XPATH, "//a[text()=\"Войти\"]")))
        browser.find_element(By.XPATH, "//a[text()=\"Войти\"]").click()
        browser.find_element(By.CSS_SELECTOR, "[name=\"login\"]").click()
        browser.find_element(By.CSS_SELECTOR, "[name=\"login\"]").send_keys("Starikowlad@gmail.com")
        browser.find_element(By.CSS_SELECTOR, "[name=\"password\"]").click()
        browser.find_element(By.CSS_SELECTOR, "[name=\"password\"]").send_keys("be3_napol9")
        browser.find_element(By.XPATH, "//button[text()=\"Войти\"]").click()
        time.sleep(5)
        WebDriverWait(browser, 300).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder=\"Напишите ваш ответ здесь...\"]")))
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]').click()
        answer = math.log(int(time.time()))
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]').send_keys(str(answer))
        browser.find_element(By.XPATH, '//button[text()="Отправить"]').click()
        time.sleep(10)
        is_correct = browser.find_element(By.CSS_SELECTOR, "[class=\"smart-hints__hint\"]")
        print(is_correct.text)
        assert 'Correct!' == is_correct.text, f"expected 'Correct!', actual {is_correct.text}"
