import json
import unittest,requests
from read_excel import *
from db import *



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.li=read_excel().excel_to_list("test_user_data.xlsx","test_user_reg")
    def test_reg_ok(self):
        case_data=read_excel().get_test_data(self.li,'reg_ok')

        url=case_data.get('url')
        args= case_data.get('args')
        expect_res=case_data.get("expect_res")
        a=json.loads(args).get("userName")
        if check_user(name=a):
            # 如果已经注册了 就删除
            del_user(a)
        res=requests.post(url=url,json=json.loads(args))
        self.assertIn(expect_res,res.text)
        del_user(a)
    def test_reg_err(self):
        case_data=read_excel().get_test_data(self.li,"reg_err")
        url=case_data.get('url')
        args=case_data.get('args')
        expect_res=case_data.get('expect_res')
        res=requests.post(url=url,json=json.loads(args))


if __name__ == '__main__':
    unittest.main()
