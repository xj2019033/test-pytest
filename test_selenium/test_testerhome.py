
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

logging.basicConfig(level = logging.INFO)
class Test_testerhome:

    @classmethod
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://testerhome.com')
        self.driver.implicitly_wait(5)
    @classmethod
    def teardown_method(self):
        #self.driver.quit()
        pass

    def test_login(self):
        self.driver.find_element(By.CSS_SELECTOR,'a[href*=sign_in]').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'user_login').send_keys('aaa')
        self.driver.find_element(By.NAME, 'user[password]').send_keys('123')
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name('commit').send_keys(Keys.ENTER)
        value=self.driver.find_element_by_css_selector('div[class*=alert-warning]').text
        logging.info(value)
        assert value=='没有该用户，请您重新注册。'

    def test_teams(self):
        self.driver.get('https://testerhome.com')
        self.driver.find_element_by_css_selector('a[href*=teams]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector('a[title*=霍格沃兹测试学院]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector('a[title*=企业微信实战_20190804]').click()
        self.driver.implicitly_wait(5)
        value = self.driver.find_element_by_css_selector('div[class*=alert-danger]').text
        logging.info(value)
        assert value == '访问被拒绝，你可能没有权限或未登录。'

    def test_search(self):
        self.driver.find_element(By.CSS_SELECTOR,'input[name=q]').send_keys('测试媛')
        self.driver.find_element(By.CSS_SELECTOR, 'input[name=q]').send_keys(Keys.ENTER)
        self.driver.implicitly_wait(3)
        #self.driver.find_element_by_xpath('//a[contains(text(),"组织成立啦")]').click()
        toptitle=self.driver.find_elements_by_css_selector('div.topic a')[0].text
        logging.info(toptitle)
        self.driver.find_elements_by_css_selector('div.topic a')[0].click()
        self.driver.implicitly_wait(3)
        title=self.driver.find_elements_by_css_selector('span.title')[1].text
        logging.info(title)
        assert toptitle==title

    def test_cookie(self):
        self.driver.add_cookie()