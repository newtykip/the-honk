word = input('Please enter a word!')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
nopunc = ''

for i in word:
    if i not in punctuations:
        nopunc = nopunc + i

def isPallindrome(x):
    return x == x[::-1]

if isPallindrome(nopunc):
    print('{0} is a pallindrome!'.format(word))
else:
    print('{0} is not a pallindrome!'.format(word))