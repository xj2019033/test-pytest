from selenium import webdriver
from selenium.webdriver.common.by import By


class Wework:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.implicitly_wait(5)
        cookies = {'wwrtx.d2st': 'a9476664',
                   'wwrtx.sid': 'doR_2fdSBlviJ1PgeZ7RnUGqcjYoSIOB6eUQGFcIXScCghROojHd8MdWvNtXavdZ',
                   'wwrtx.ltype': '1',
                   'wxpay.corpid': '1970324943086403',
                   'wxpay.vid': '1688853484961678',
                   'wwrtx.vst': 'kHlhsAXFkvJc-2fqQWzXqfXFuJ9AyY86JkIal7-84Jbzezw_HiZWDhzsSUZwNaSVcbRktuMfPDmHD_Tpb6eqjT1eY9YIlyTa4SRiogJlwzF_md8ybjc5m8J5vllWE-VFZBLnYQkw-SN58H14aWBbeY2qsVsG3GcV9ccVD0h-kulwwr6j2z8AlS_OQw0CCghU49fcW8QqWeEWv7FvDIamSRrfrv4WggNkPKUbeNdmkfIY1Uc1gr8lDg5x-Jkri8RRl2t884_Nn3kdHGKcD3pipw'
                   }

        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    def goto_contactpage(self):
        self.driver.find_element(By.CSS_SELECTOR,'a#menu_contacts').click()

    def goto_managepage(self):
        self.driver.find_element(By.ID,'menu_manageTools').click()



    def quit(self):
        self.driver.quit()


