import urllib.request

guessed = []
correct = []

# Get a word from the API
word = urllib.request.urlopen('http://random-word-api.herokuapp.com/word?number=1').read().decode()
word = str(word[2:len(word)-2])
print(word)

lives = 6
letters = []
for i in word:
    letters.append(i)

while lives != 0:
    # Take in a guess
    letter = input('Please enter a letter: ').lower()
    # Ensure that the letter is valid, and has not already been guessed
    if len(letter) > 1 or letter.isnumeric():
        print('That is not a letter!')
        continue
    if letter in guessed:
        print('You have already guessed \'{0}\'!'.format(letter))
        continue
    # Ensure that the letter is in the word - if not, subtract a life
    if letter in word:
        correct.append(letter) # Add the letter to the correct list
        # If the unordered list of correct letters is the same as the unordered list of letters in the word, the player wins
        if set(correct) == set(letters):
            print('You won, with {0} lives to spare! The word was {1}'.format(str(lives), word))
            lives = 0
    else:
        lives -= 1
        print('Uh oh! \'{0}\' is wrong! You have {1} lives left.'.format(letter, str(lives)))

    guessed.append(letter)