below = 1000
multiplesOf = [3,5]
toAdd = []

for i in range(1, below):
	for num in multiplesOf:
		if i % num == 0:
			toAdd.append(i)

toAdd = list(dict.fromkeys(toAdd))
total = 0

for i in toAdd:
	total += i

print(total)
