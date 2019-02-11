import unittest
from FizzBuzzGenerator import isValidInput,isInputGreaterThan5,isInputDivisibleBy3,isInputDivisibleBy5

class FizzBuzzGeneratorTestClass(unittest.TestCase):
    """Tests for `FizzBuzzGenerator.py`."""

    def test_is_valid_input(self):
        """Is x a valid input"""
        self.assertTrue(isValidInput(3))
        self.assertFalse(isValidInput("abc"))


    def test_is_input_greater_than_5(self):
        self.assertTrue(isInputGreaterThan5(6))
        self.assertTrue(isInputGreaterThan5(5))
        self.assertFalse(isInputGreaterThan5(3))

    def test_is_input_divisible_by_3(self):
    	self.assertFalse(isInputDivisibleBy3(4))
    	self.assertTrue(isInputDivisibleBy3(9))

   	def test_is_input_divisible_by_5(self):
   		self.assertFalse(isInputDivisibleBy5(6))
    	self.assertTrue(isInputDivisibleBy5(10))


if __name__ == '__main__':
    unittest.main()