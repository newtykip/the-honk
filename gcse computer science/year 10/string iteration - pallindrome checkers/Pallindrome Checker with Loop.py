word = input('Please enter a word!')

def isPallindrome(x):
    reverse = ''
    i = len(x)
    while i > 0:
        reverse += x[i - 1]
        i = i - 1
    return x == reverse

if isPallindrome(word):
    print('{0} is a pallindrome!'.format(word))
else:
    print('{0} is not a pallindrome!'.format(word))