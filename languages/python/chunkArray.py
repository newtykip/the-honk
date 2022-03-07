def chunkArray(array, chunkCount):
	chunks = []

	for i in reversed(range(1, chunkCount + 1)):
		splitPoint = len(array) // i
		chunks.append(array[:splitPoint])
		array = array[splitPoint:]
	
	return chunks

print(chunkArray([1,2,3,4,5,6], 3))
