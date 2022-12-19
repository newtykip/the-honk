mapping = {
	':)': '🙂',
	':(': '🙁'
}

text = input('Please enter some text: ')

for emoticon in mapping.keys():
	text = text.replace(emoticon, mapping[emoticon])

print(text)
