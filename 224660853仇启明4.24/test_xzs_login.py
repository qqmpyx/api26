import json
import unittest,requests
from read_excel import *

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.li=read_excel().excel_to_list("test_user_data.xlsx","test_user_login")

    def test_login_ok(self):
        case_data = read_excel().get_test_data(self.li, 'login_ok')
        url = case_data.get('url')
        args = case_data.get('args')
        expect_res = case_data.get("expect_res")
        json.loads(args).get("userName")


    def test_login_err1(self):
        case_data=read_excel().get_test_data(self.li,'login_err1')
        #case_data['url']
        url=case_data.get('url')

    def test_login_err2(self):
        case_data=read_excel().get_test_data(self.li,'login_err2')
        #case_data['url']
        url=case_data.get('url')

    def test_login_err3(self):
        case_data=read_excel().get_test_data(self.li,'login_err3')
        #case_data['url']
        url=case_data.get('url')

if __name__ == '__main__':
    unittest.main()

