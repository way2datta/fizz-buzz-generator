#FizzBuzzGenerator.py

def isValidInput(input):
	return type(input) == int

def isInputGreaterThan5(input):
	return input >= 5

def isInputDivisibleBy3(input):
	return input%3 == 0

def isInputDivisibleBy5(input):
	return input%5 == 0

def printFizzIfInputIsDivisibleByOnly3(input):
	if isInputDivisibleBy3(input) and not(isInputDivisibleBy5(input)):
		return "fizz"

def printBuzzIfInputIsDivisibleByOnly5(input):
	if not(isInputDivisibleBy3(input)) and isInputDivisibleBy5(input):
		return "buzz"