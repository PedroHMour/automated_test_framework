import pytest
from selenium import webdriver
from seleniun.webdriver.common.by import By
from utils.browser import Browser


class TestSearch:
    def setup_method(self):
        self.driver = Browser.start_browser()

    def teardown_method(self):
        self.driver.quit()

    def test_search_item(self):
        self.driver.get('https:/example.com')
        self.driver.find_element(By.NAME, 'q').send_keys('Item test')
        self.driver.find_element(By.ID, 'search_button').click()

        results = self.driver.find_elements(By.CLASS_NAME, 'results_item')
        assert len(results) > 0, "No results found"        