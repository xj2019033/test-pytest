import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Testselenium:
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_browser(self):
        self.driver.get('https://testerhome.com')

    def test_search(self):
        self.driver.get('https://testerhome.com')
        #time.sleep(5)

        #ActionChains()
