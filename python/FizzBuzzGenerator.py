#FizzBuzzGenerator.py
import string
import sys

class FizzBuzzGenerator:

	def validateInput(self,input):
		if type(input) == int:
			if input > 0:
				return True
			else:
				return None
		else:
			return None
	
	def fizzBuzzGenerator(self,input):
		if self.validateInput(input):
			if input%3 == 0 and not(input%5 == 0):
				return "fizz"
			if input%5 == 0 and not(input%3 == 0):
				return "buzz"
			if input%3 == 0 and input%5 == 0:
				return "fizzbuzz"
			if not(input%3 == 0) and not(input%5 == 0):
				return str(input)
		else:
			return None

if __name__ == '__main__':
	main()