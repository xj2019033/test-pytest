from selenium.webdriver.common.by import By

from test_po.base_page import BasePage
from test_po.wework_page import Wework


class ManageTools(BasePage):

    def __init__(self,wework:Wework):
        self._driver=wework.driver
        wework.goto_managepage()

    def goto_descpage(self):
        ss='js_manageTools_index > div > ul > li:nth-child(5) > a > div > div.manageTools_cnt_item_desc_title'
        self._driver.implicitly_wait(5)
        self._driver.find_element(By.CSS_SELECTOR,ss).click()
        #return DescPage(self._driver)