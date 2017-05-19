"""This is a program to test add_ing_v1.py and add_ing_v2.py

As of now we need import add_ing_v1 or add_ing_v2 to run
unittest on either code.
"""
import unittest
from add_ing_v1 import *
#from add_ing_v2 import *

class add_ing_test_case(unittest.TestCase):

    def test_verb_end_e(self):
        self.assertFalse(isVerbends_with_e("sit"))
        self.assertTrue(isVerbends_with_e("double"))
        self.assertFalse(isVerbends_with_e("end"))
        self.assertFalse(isVerbends_with_e("comb"))

    def test_verb_consonent(self):
        self.assertFalse(isVerbConsonent("end"))
        self.assertTrue(isVerbConsonent("sit"))
        self.assertFalse(isVerbConsonent("double"))
        self.assertFalse(isVerbConsonent("comb"))

    def test_add_ing(self):
        self.assertEqual("ending", add_ing("end"))
        self.assertEqual("sitting", add_ing("sit"))
        self.assertEqual("doubling", add_ing("double"))
        self.assertEqual("combing", add_ing("comb"))


if __name__ == '__main__':
    unittest.main()

# suite = unittest.TestLoader().loadTestsFromTestCase(add_ing_test_case)
# unittest.TextTestRunner(verbosity=2).run(suite)
