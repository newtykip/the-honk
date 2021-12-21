def count1(n):
	x = str(n)
	count = 0
	for index, digit in enumerate(x[::-1]):
		digit = int(digit)
		if digit != 0:
			if digit == 1:
				numberAfter = x[len(x) - index:] or '0'
				count += int(numberAfter) + 1
			else:
				count += 10 ** index
		count += int(10 ** (index - 1) * index * digit)
	return count


print(count1(3**35))
