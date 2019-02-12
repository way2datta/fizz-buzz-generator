from app import appCode

class testClass:

	def callOtherClassMethod(self):
		self.app_instance.printAppString("shadja")
		print("chaudhari")

	def callabove(self):
		callOtherClassMethod()


def main():
	testClass_instance = testClass()
	testClass_instance.callabove()
	appCode_instance = appCode()

if __name__ == '__main__':
	main()