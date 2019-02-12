from FizzBuzzGenerator import FizzBuzzGenerator

class FizzBuzzGeneratorTestClass(unittest.TestCase):
    		
	def test_is_valid_input(self):
		fizzbuzzgenerator = FizzBuzzGenerator()
		self.assertEquals(None,fizzbuzzgenerator.fizzBuzzGenerator(0))