from string import ascii_lowercase

def abacaba(n):
	output = ''
	currLetter = 0
	for i in range(n):
		output = '{0}{1}{2}'.format(output, ascii_lowercase[currLetter], output)
		currLetter = currLetter + 1
		if currLetter > 25:
			currLetter = 0
	return output

out = abacaba(10)
print(out)
