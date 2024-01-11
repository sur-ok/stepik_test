from test.pages.locators import MainPageLocators
from test.pages.base_page import BasePage
from test.pages.login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        # self.browser.find_element(By.CSS_SELECTOR, '#login_invalid')
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link is not presented"

