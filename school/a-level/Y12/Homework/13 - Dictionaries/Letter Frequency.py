from typing import Dict
import re

def letterFrequency(text: str) -> Dict[str, int]:
	output = {}
	text = re.sub('[^a-zA-Z]+', '', text)

	for letter in text:
		if letter in output:
			output[letter] += 1
		else:
			output[letter] = 1

	return output

frequency = letterFrequency('I wish I wish with all my heart to fly with dragons in a land apart')
print(frequency)
