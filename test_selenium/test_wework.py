import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level = logging.INFO)
class Test_testerhome:

    @classmethod
    def setup_method(self):
        #Chrome_option=webdriver.ChromeOptions()
        #Chrome_option.debugger_address="127.0.0.1:9222"
        #self.driver=webdriver.Chrome(options = Chrome_option)
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#material/image')
        self.driver.implicitly_wait(5)
    @classmethod
    def teardown_method(self):
        #self.driver.quit()
        pass
    def test_upload_file(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#material/image')
        element_add=self.driver.find_element(By.CSS_SELECTOR,'.js_upload_file_selector')
        self.driver.execute_script("arguments[0].click()",element_add)
        self.driver.find_element(By.CSS_SELECTOR,'#js_upload_input')\
            .send_keys(r'D:\测试视频库\1所有车牌\20181112011007_晋V811B0_轿车.jpg')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel")))
        self.driver.find_element(By.CSS_SELECTOR,'a[d_ck=submit]').click()

    def test_contacts(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        self.driver.implicitly_wait(3)
        self.driver.find_elements(By.CSS_SELECTOR,'.js_add_member')[1].click()
        self.driver.find_element(By.ID,'username').send_keys('xxxx')
        self.driver.find_element(By.ID,'memrAdd_acctid').send_keys('xxxx')
        self.driver.find_element(By.ID,'membeberAdd_mail').send_keys('123@dd.com')
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()

    def test_cookies(self):
        cookies = {'wwrtx.d2st': 'a3342515',
                   'wwrtx.sid': 'doR_2fdSBlviJ1PgeZ7RnaIjLFIOmTyPEoqxSrDsefaJDFrwu-VQJlc13ISNrxjM',
                   'wwrtx.ltype': '1',
                   'wxpay.corpid': '1970324943086403',
                   'wxpay.vid': '1688853484961678',
                   'wwrtx.vst': '-5p_PGczL_h4Bc6w2-MAh7sl2WBwpRKrmD4Y_c28FZx7O5G4nGD3CaqUR9qXtebWq5MEYZQ3kyN6O9U2C0xxTl5Tfp9HwBDHpVpv-J5GJcEARBsTRetMft16dgG9NflCu2BicvYfkJNMTrb7jxIAYqQ7yXxWxVaGCDu0YvAX9AIkMABohVgrhUGYU-wDVwYj20Gb951D73yLIDKpBXd8vOEUVw6_T0QOzQd5LbA4V0XM80ndy1XQRCZuQ1NxLpXejeAAWKIv3-GFFzgp5CAeSw'
                   }

        for k,v in cookies.items():
            self.driver.add_cookie({"name":k,"value":v})
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#material/image')