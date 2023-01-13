from path import *
from src.appdemo import verify
import unittest

class UnitTests(unittest.TestCase):

    def test_PositiveValue(self):
        actual = verify(5)
        expected = "Good accepted value"
        self.assertEqual(actual, expected, "Good accepted value")
    def test_NegativeValue(self):
        actual = verify(-5)
        expected = "Value not accepted"
        self.assertEqual(actual, expected, "Value not accepted")
    def test_NotIntValue(self):
        actual = verify("fsdsss")
        expected = "Verify your input"
        self.assertEqual(actual, expected, "Verify your input")
        
if __name__ == "__main__":
    unittest.main()
