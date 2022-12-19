while True:
	try:
		pounds = input('How much was the meal? ')

		pounds = pounds.split('£')
		pounds = pounds[len(pounds) - 1]
		pounds = float(pounds)

		break
	except ValueError:
		print('Please ensure that you input a valid amount of money!')

while True:
	try:
		percentage = input('What percentage would you like to tip? ')

		percentage = percentage.split('%')[0]
		percentage = float(percentage) / 100

		break
	except ValueError:
		print('Please ensure that you enter a valid percentage!')

tip = round(pounds * percentage, 2)
print(f'You should tip £{tip}!')
