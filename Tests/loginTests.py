import time
from selenium import webdriver
from Pages.loginPage import LoginPage


class LoginTest:
    def setup_method(self):
        self.driver = webdriver.Chrome()  # Initialize WebDriver
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        try:
            self.login_page.enter_username("Admin")
            self.login_page.enter_password("admin123")
            self.login_page.click_login()
            time.sleep(3)
            self.login_page.assert_any("OrangeHRM")
            time.sleep(3)
            self.login_page.find_element_in_new_tab()
            time.sleep(5)
            self.login_page.switch_back_to_first_tab()  # Switch back to the first tab
            time.sleep(5)
            print("login test passed")
        except Exception as e:
            print(f"Login test failed {e}")


# Run the test
test = LoginTest()
test.setup_method()
test.test_login()



#
# import time
# from selenium import webdriver
# from Pages.loginPage import LoginPage
#
#
# class LoginTest:
#     def setup_method(self):
#         self.driver = webdriver.Chrome()  # Initialize WebDriver
#         self.driver.maximize_window()
#         self.login_page = LoginPage(self.driver)
#
#     @staticmethod
#     def test_login():
#         try:
#             test_instance = LoginTest()
#             test_instance.setup_method()
#             test_instance.login_page.enter_username("Admin")
#             test_instance.login_page.enter_password("admin123")
#             test_instance.login_page.click_login()
#             time.sleep(3)
#             test_instance.login_page.assert_any("OrangeHRM")
#             time.sleep(3)
#             test_instance.login_page.find_element_in_new_tab()
#             time.sleep(5)
#             print("login test passed")
#         except Exception as e:
#             print(f"Login test failed {e}")
#
#
# # Run the test
# LoginTest.test_login()