# helper method to easily take in float inputs
def floatInput(text):
	while True:
		try:
			x = float(input(text))
			return x
		except ValueError:
			print('You must input a float!\n')
