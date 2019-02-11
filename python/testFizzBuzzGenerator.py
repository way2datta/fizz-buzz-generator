import unittest
from FizzBuzzGenerator import isValidInput,isInputGreaterThan3,isInputDivisibleBy3

class FizzBuzzGeneratorTestClass(unittest.TestCase):
    """Tests for `FizzBuzzGenerator.py`."""

    def test_is_valid_input(self):
        """Is x a valid input"""
        self.assertTrue(isValidInput(3))
        self.assertFalse(isValidInput("abc"))


    def test_is_input_greater_than_3(self):
        self.assertTrue(isInputGreaterThan3(4))
        self.assertFalse(isInputGreaterThan3(2))

    def test_is_input_divisible_by_3(self):
    	self.assertFalse(isInputDivisibleBy3(4))
    	self.assertTrue(isInputDivisibleBy3(9))


if __name__ == '__main__':
    unittest.main()