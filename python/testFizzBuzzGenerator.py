import unittest
from FizzBuzzGenerator import FizzBuzzGenerator

class FizzBuzzGeneratorTestClass(unittest.TestCase):
    		
  def test_is_valid_input(self):
    fizzbuzzgenerator = FizzBuzzGenerator()
    self.assertEquals(None,fizzbuzzgenerator.fizzBuzzGenerator(0))
    
  def test_fizz_if_input_divisible_by_3(self):
    fizzbuzzgenerator = FizzBuzzGenerator()
    self.assertEquals("fizz",fizzbuzzgenerator.fizzBuzzGenerator(3))

if __name__ == '__main__':
    unittest.main()