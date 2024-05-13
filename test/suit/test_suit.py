import unittest,sys
sys.path.append("../..")
from test.case.user.test_user_login import test_user_login
from test.case.user.test_user_reg1 import test_user_reg


# smoke_suit=unittest.TestSuite()
# smoke_suit.addTest(test_user_login('test_login'))
# smoke_suit.addTest(test_user_reg('test_reg1'))
# def get_suite(suit_name):
#     return globals().get(suit_name)
#
#
# unittest.texTestRunner(verbosity=2).run(smoke_suit)
def get_suit(suit_name):
    suit_name=unittest.TestSuite()
    suit_name.addTests([test_user_login('test_login_fail'),test_user_reg('test_user_red_fail')])
    return suit_name
