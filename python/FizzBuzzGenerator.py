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
        