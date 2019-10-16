from test_po.desc_page import DescPage
from test_po.wework_page import Wework


class TestDesc:

    def setup(self):
        self.work=Wework()
        self.desc=DescPage(self.work)

    def test_add_pic(self):
        self.desc.add_pic(r'D:\测试视频库\1所有车牌\20181112011007_晋V811B0_轿车.jpg')