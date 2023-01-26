# helper method to easily take in float list inputs
def listInput(text, delimeter = ','):
	while True:
		try:
			x = input('%s - the delimeter is %s (:\n' % (text, delimeter))
			x = x.split(delimeter)
			nums = [float(a) for a in x]
			return nums
		except ValueError:
			print('All of the values must be floats!')
