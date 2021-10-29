sequence = [1, 2]

while sequence[len(sequence) - 1] < 4000000:
	sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2])
sequence.pop()

total = 0

for i in sequence:
	if i % 2 == 0:
		total += i

print(total)
