from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class test_add_to_cart:
    burger_menu = (By.ID, "react-burger-menu-btn")
    burger_menu_close = (By.ID, "react-burger-cross-btn")
    add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.chains = ActionChains(driver)

    def open_burger_menu(self):
        self.wait.until(EC.visibility_of_element_located(self.burger_menu)
                        ).click()

    def close_burger_menu(self):
        self.wait.until(EC.visibility_of_element_located(self.burger_menu_close)
                        ).click()

    def add_to_cart_item(self):
        self.wait.until(EC.visibility_of_element_located(self.add_to_cart)
                        ).click()
