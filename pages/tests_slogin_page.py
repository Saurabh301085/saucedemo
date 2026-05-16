from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class test_login_page1:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    button = (By.XPATH, "//input[@type='submit']")
    error_msg = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_input)
                        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input)
                        ).send_keys(password)

    def login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.button))
        login_button.click()

    def is_product_page_loaded(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))
                               )

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text
