c = 299792458

while True:
	try:
		m = int(input('Please enter an integer mass in kg: '))
		break
	except ValueError:
		print('Please ensure that your input was an integer!')

e = m * (c ** 2)
print(f'e = {e:,}J')
