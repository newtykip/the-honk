import re

word = input('Please enter a word!')

def isPallindrome(word):
    # Strip the word of punctuation
    word = re.sub(r'[^\w\s]', '', word)

    # Check if the word is a pallindrome
    reverse = ''
    i = len(word)

    while i > 0:
        reverse += word[i - 1]
        i = i - 1

    return word == reverse

if isPallindrome(word):
    print('{0} is a pallindrome!'.format(re.sub(r'[^\w\s]', '', word)))
else:
    print('{0} is not a pallindrome!'.format(re.sub(r'[^\w\s]', '', word)))
