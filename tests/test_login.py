import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browser import Browser


class Testlogin:
    def setup_method(self):
        self.driver = Browser.start_browser()

    def teardown_method(self):
        self.driver.quit()

    def test_valid_login(self):
        self.driver.get('https://example.com/login')
        self.driver.find_element(By.ID, 'username').send_keys('valid_user')
        self.driver.find_element(By.ID, 'password').send_keys('valid_password')
        self.driver.find_element(By.ID, 'login_button').click()

        assert "Dashboard" in self.driver.title, "Login failed"

    def test_invalid_login(self):
        self.driver.get('https:/example.com/login')
        self.driver.find_element(By.ID, 'username').send_keys('invalid_user')
        self.driver.find_element(By.ID, 'password').send_keys('invalid_password')
        self.driver.find_element(By.ID, 'login_button').click()

        error_message = self.driver.find_element(By.ID, 'error_message').text
        assert "Invalid credentials" in error_message, "Error message not displayed"
                