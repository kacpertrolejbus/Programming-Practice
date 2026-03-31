import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
    

class InputTesting(TestCase):
    BLOG_URL = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrVS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNSy0v1k9JTUsszSlRsgYAc345de1b2b3fe0e9b09387e31ed359621a1f4e56&locale=pl"
    INPUT_NAME = "username"
    INPUT_PASSWORD = "password"
    INPUT_BUTTON = "clear"

    def test_input_value(self):
        self.driver.get(self.BLOG_URL)
        try:
            login_box = self.driver.find_element(by=By.NAME, value=self.INPUT_NAME)
        except Exception:
            self.fail("Login input not found!")
        
        login_box.send_keys("your_username")
        inputValue = login_box.get_attribute("value")
        self.assertEqual("your_username", inputValue)

    def test_clear_button(self):
        self.driver.get(self.BLOG_URL)
        try:
            login_box = self.driver.find_element(by=By.NAME, value=self.INPUT_NAME)
            password_box = self.driver.find_element(by=By.NAME, value=self.INPUT_PASSWORD)
            clear_button = self.driver.find_element(by=By.NAME, value=self.INPUT_BUTTON)
            login_box.send_keys("your username")
            password_box.send_keys("password")
            clear_button.click()
        except Exception:
            self.fail("Error!")
        
        input_login = login_box.get_attribute("value")
        self.assertEqual("", input_login)
        input_password = password_box.get_attribute("value")
        self.assertEqual("", input_password)


