import math
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from test.pages.base_page import BasePage
from test.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_product(self):
        self.browser.find_element(*ProductPageLocators.ADD_PRODUCT).click()

    def check_book(self):
        assert self.browser.find_element(*ProductPageLocators.TEXT_BOOK).text == \
               self.browser.find_element(*ProductPageLocators.TEXT_BOOK_ON_ALERT).text
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_BUSKET_ON_ALERT).text

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
