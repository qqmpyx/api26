import unittest,requests
from lib.p2p import *
proNum="22"
proNum1="78"
data = {"proNum":"22","proName":"22","proLimit":"22","annualized":"%"}
data1 = {"proNum":"778","proName":"778","proLimit":"778","annualized":"778"}

class MyTestCase(unittest.TestCase):
    url = "http://192.168.55.24:8085/p2p_management/addProduct"
    # 判断 proNum1是否已经注册过，注册过删除
    def test_ok_1(self):
        if check_user(proNum1):
            del_user(proNum1)
        data1 = {"proNum":"778","proName":"778","proLimit":"778","annualized":"778"}
        a = requests.post(url=self.url, json=data1)
        # 判断数据库中proNum1已经存在
        self.assertTrue(check_user(proNum1))
        # 数据还原
        del_user(proNum1)
    def test_ok_2(self):
        if check_user(proNum):
            add_user("22","22","22","22")
        a = requests.post(url=self.url,json=data)
        self.assertIn("400",a.text)
if __name__ == '__main__':
    unittest.main()
