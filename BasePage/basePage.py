from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(by_locator)).clear()
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(by_locator)).send_keys(text)

    def assert_any(self, title):
        assert title in self.driver.title

    def switch_to_new_tab(self, by_locator):
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(by_locator)).click()

    def switch_back_to_first_tab(self):
        original_window = self.driver.window_handles[0]
        self.driver.switch_to.window(original_window)
