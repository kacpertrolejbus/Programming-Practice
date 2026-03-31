import unittest

from main import *

class Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""), 0)
    def test_one_arg(self):
        self.assertEqual(Add("1"), 1)
    def test_two_arg(self):
        self.assertEqual(Add("1, 2"), 3)
    def test_more_than_two_arg(self):
        self.assertEqual(Add("2,5,1"), 8)
    def test_value_error(self):
        with self.assertRaises(ValueError):
            Add("r,7")
    def test_new_line(self):
        self.assertEqual(Add("1\n3"),4)
    def test_new_line_error(self):
        with self.assertRaises(ValueError):
            Add("1,\n")
