import unittest
from calculate.operators import Operators

class TestOperators(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Operators().addition("3+3"), 6)

    def test_bad_format(self):
        self.assertIsNone(Operators().addition("3++3"))