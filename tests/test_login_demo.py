import time

from selenium.webdriver.chrome import options

from SauceDemo.pages.tests_slogin_page import test_login_page1
from SauceDemo.pages.test_product_page import test_add_to_cart


class Test_login_dtls:

    def test_sauce(self, driver):
        sauce = test_login_page1(driver)
        sauce.enter_username("standard_user1")
        sauce.enter_password("secret_sauce")
        sauce.login()
        assert sauce.is_product_page_loaded()

        sauce.enter_username("wrong_user")
        sauce.enter_password("wrong_pass")
        sauce.login()

        error= sauce.error_msg()
        assert "Username and password do not match" in error

        time.sleep(4)

        # product = test_add_to_cart(driver)
        # # options.add_argument("--disable-save-password-bubble")
        # # options.add_argument("--disable-extensions")
        # product.open_burger_menu()
        # product.close_burger_menu()
        # product.add_to_cart_item()
