#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/17 16:21
# Author : smart
# @File : 4.17.1.py
# @Software : PyCharm
import unittest
def setUpModule():
    print('=== setUpModule ===')
def tearDownModule():
    print('=== tearDownModule ===')
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass")
    @classmethod
    def tearDownClass(cls):
        print("teardownclass")
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    def test_01(self):
        print('test01')
        #完全相等
        self.assertEqual(True, True)
    def test_02(self):
        print('test02')
        #包含 a包含在b中
        self.assertIn('h', 'hello')

    def test_03(self):
        print('test03')
        # 判断他们的内存地址是否是一样的
        self.assertIsNot(1, 1/1)
    def test_04(self):
        print('test04')
        #比大小
        self.assertLess(3,4)
    def test_05(self):
        print('test05')
        #判断类型
        # self.assertIsInstance([1,2],list)
        self.assertIsInstance({'user':'su','ps':123},dict)


if __name__ == '__main__':
    unittest.main()