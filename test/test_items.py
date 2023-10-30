from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_items:
    def test_clickable_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        assert WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add_to_basket_form")))