sentence = str(input('Please input a sentence.'))
words = sentence.split()
theCount = 0

for word in words:
    if str.lower(word) == 'the':
        theCount = theCount + 1

print('"The" appears ', theCount, " times.")