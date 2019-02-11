import unittest
from FizzBuzzGenerator import printInputAsStringIfInputIsNotDivisibleBy3And5,isValidInput,isInputGreaterThan5,isInputDivisibleBy3,isInputDivisibleBy5,printFizzIfInputIsDivisibleByOnly3,printBuzzIfInputIsDivisibleByOnly5,printBuzzIfInputIsDivisibleBy3And5
#import FizzBuzzGenerator
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

    def test_output_equals_fizz_if_input_is_divisible_only_by_3(self):
    	self.assertEquals("fizz",printFizzIfInputIsDivisibleByOnly3(6))
    	self.assertNotEquals("fizz",printFizzIfInputIsDivisibleByOnly3(15))

    def test_output_equals_buzz_if_input_is_divisible_only_by_5(self):
    	self.assertEquals("buzz",printBuzzIfInputIsDivisibleByOnly5(10))
    	self.assertNotEquals("buzz",printBuzzIfInputIsDivisibleByOnly5(15))

    def test_output_equals_fizzbuzz_if_input_is_divisible_3_and_5(self):
    	self.assertEquals("fizzbuzz",printBuzzIfInputIsDivisibleBy3And5(15))
    	self.assertNotEquals("fizzbuzz",printBuzzIfInputIsDivisibleBy3And5(9))
    	self.assertNotEquals("fizzbuzz",printBuzzIfInputIsDivisibleBy3And5(10))

    def test_output_equals_number_as_string_if_input_is_not_divisible_by_3_and_5(self):
    	self.assertEquals("4",printInputAsStringIfInputIsNotDivisibleBy3And5(4))
    	self.assertNotEquals("4",printInputAsStringIfInputIsNotDivisibleBy3And5(9))
    	self.assertNotEquals("10",printInputAsStringIfInputIsNotDivisibleBy3And5(10))
    	self.assertNotEquals("15",printInputAsStringIfInputIsNotDivisibleBy3And5(15))

if __name__ == '__main__':
    unittest.main()