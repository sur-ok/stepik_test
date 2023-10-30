import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_items:
    def test_visible_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(10)
        assert WebDriverWait(browser, 300).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add_to_basket_form")))
