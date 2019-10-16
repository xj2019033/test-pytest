from selenium.webdriver.common.by import By

from test_po.base_page import BasePage
from test_po.contact_page import ContactPage
from test_po.wework_page import Wework


class SearchPage(BasePage):
    _edit=(By.CSS_SELECTOR,'a.js_edit')
    _disable=(By.CSS_SELECTOR,'a.js_disable')
    _username=(By.ID,'username')
    _englishname=(By.NAME,'english_name')


    def __init__(self,wework:Wework):
        self._driver=wework.driver
        wework.goto_contactpage()
        self.contact=ContactPage(wework)

    def search(self,searchname):
        self.contact.search(searchname)

    def edit(self,username,englishname):
        self._driver.implicitly_wait(5)
        self.find(self._edit).click()
        self.find(self._username).clear()
        self.find(self._username).send_keys(username)
        self.find(self._englishname).clear()
        self.find(self._englishname).send_keys(englishname)
        return self

    def disable(self):
        self.find(self._disable).click()

    def able(self):
        self.find(self._disable).click()




