def pascal(rowCount):
	rows = [[1]]

	for _ in range(rowCount): 
		previousRow = rows[-1]
		newRow = [1] # starts with a 1
		for j in range(len(previousRow) - 1): 
			newRow.append(previousRow[j] + previousRow[j + 1]) 
		newRow.append(1) # ends with a 1 
		rows.append(newRow)

	return rows

def nthRow(n):
	rows = pascal(n)
	return rows[n]

print(nthRow(10))
