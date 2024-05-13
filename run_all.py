import time
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suit import *
#
# class MyTestCase(unittest.TestCase):
#     def test_all(self):
#         logging.info('=================运行所有的case=================')
#         suit = unittest.defaultTestLoader.discover(test_path,'test*.py')
#         t = time.strftime('%Y_%m_%d_%H_%M_%S')
#         with open(report_file, 'wb') as f:
#             HTMLTestRunner(
#                 stream=f,
#                 title='xzs测试用例',
#                 description='xzs登录和注册用例集',
#                 verbosity=2
#             ).run(suit)
#
#         send_email(report_file)
#         logging.info('===========测试结束=============')
# if __name__ == '__main__':
#     unittest.main()
def discover():
    return unittest.defaultTestLoader.discover(test_case_path)
def run(suite):
    logging.info('==== 测试开始 ====')
    with open(report_file,'wb') as f:
        HTMLTestRunner(
            stream=f,
            title='接口测试',
            description='测试描述',
            verbosity=2,
            # tester='smart'
        ).run(suite)
    logging.info('==== 测试结束 ====')
def run_all():
    run(discover())
def run_suite(suite_name):
    suite = get_suit(suite_name)
    if isinstance(suite,unittest.TestSuite):
        run(suite)
    else:
        print('TestSuite不存在')

def collect():
    suite = unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
    return suite

def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i),case.id()))
    print("-----------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time() - t0))

if __name__ == '__main__':
    collect_only()

