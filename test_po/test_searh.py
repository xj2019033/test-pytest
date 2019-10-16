from test_po.contact_page import ContactPage
from test_po.search_page import SearchPage
from test_po.wework_page import Wework


class TestSearch:

    def setup(self):
        self.work=Wework()
        self.search=SearchPage(self.work)

    def test_username(self):
        self.search.search('xxx')
        self.search.edit('ddd','fff')
