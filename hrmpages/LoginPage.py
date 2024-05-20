from selenium.webdriver.common.by import By

from hrmhelper.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):
    email_ele = (By.NAME, "username")
    password_ele = (By.NAME, "password")
    loginButton_ele = (By.CSS_SELECTOR, "[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.web_element_enter(self.email_ele, username)
        self.web_element_enter(self.password_ele, password)
        self.web_element_click(self.loginButton_ele)
