from selenium.webdriver.common.by import By

from test_po.base_page import BasePage
from test_po.managetools_page import ManageTools
from test_po.wework_page import Wework


class DescPage(BasePage):
    _addpic=(By.CSS_SELECTOR,'a[herf*=image]')

    def __init__(self,wework:Wework):
        self._driver=wework.driver
        self.managetool=ManageTools(wework)

    def add_pic(self,path):
        self.managetool.goto_descpage()
        self.find(self._addpic).click()
        self._driver.find_element(By.CSS_SELECTOR,'a.js_upload_file_selector').click()
        self._driver.find_element(By.CSS_SELECTOR, '#js_upload_input').send_keys(path)

