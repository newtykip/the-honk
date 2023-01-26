# helper method to easily take in int inputs
def intInput(text):
	while True:
		try:
			x = int(input(text))
			return x
		except ValueError:
			print('You must input an integer!\n')
