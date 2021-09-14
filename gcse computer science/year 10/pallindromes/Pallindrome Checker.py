word = input('Please enter a word!')

def isPallindrome(x):
    return x == x[::-1]

if isPallindrome(word):
    print('{0} is a pallindrome!'.format(word))
else:
    print('{0} is not a pallindrome!'.format(word))