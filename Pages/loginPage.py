from selenium.webdriver.common.by import By
from BasePage.basePage import BasePage


class LoginPage(BasePage):
    # locators
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    new_tab_locator = (By.XPATH, "//a[normalize-space()=\"OrangeHRM, Inc\"]")  # New locator

    def __init__(self, driver):         # object banaune bitikai call hunxa so driver instance ta chainxa ni ta so
        super().__init__(driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self, username):
        self.enter_text(self.username_field, username)

    def enter_password(self, password):
        self.enter_text(self.password_field, password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def find_element_in_new_tab(self):
        self.switch_to_new_tab(self.new_tab_locator)
        # return element

    def navigate_back_to_first_tab(self):
        self.switch_back_to_first_tab()

