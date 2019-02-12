import unittest

from FizzBuzzGenerator import FizzBuzzGenerator

class FizzBuzzGeneratorTestClass(unittest.TestCase):
		
	def test_is_valid_input(self):
		fizzbuzzgenerator = FizzBuzzGenerator()
		self.assertEquals("fizz",fizzbuzzgenerator.fizzBuzzGenerator(3))
		self.assertEquals(None,fizzbuzzgenerator.fizzBuzzGenerator("abc"))
		self.assertEquals(None,fizzbuzzgenerator.fizzBuzzGenerator(0))

	def test_is_input_divisible_by_3(self):
		fizzbuzzgenerator = FizzBuzzGenerator()
		self.assertEquals("fizz",fizzbuzzgenerator.fizzBuzzGenerator(9))

	def test_is_input_divisible_by_5(self):
		fizzbuzzgenerator = FizzBuzzGenerator()
		self.assertEquals("buzz",fizzbuzzgenerator.fizzBuzzGenerator(10))

	def test_output_equals_fizzbuzz_if_input_is_divisible_3_and_5(self):
		fizzbuzzgenerator = FizzBuzzGenerator()		
		self.assertEquals("fizzbuzz",fizzbuzzgenerator.fizzBuzzGenerator(15))

	def test_output_equals_number_as_string_if_input_is_not_divisible_by_3_and_5(self):
		fizzbuzzgenerator = FizzBuzzGenerator()
		self.assertEquals("8",fizzbuzzgenerator.fizzBuzzGenerator(8))

if __name__ == '__main__':
    unittest.main()