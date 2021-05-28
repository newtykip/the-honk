import math
import string
import re

def encryptChar(char, key):
    # check if the character is a letter
    if re.match('^[a-zA-Z]*$', char):
        # figure out the position of the character in the alphabet
        position = string.ascii_lowercase.index(char.lower()) + 1
        # encrypt the character
        return math.ceil((position ** 2) + int(key))
    # if the character is not a letter, just return it
    else:
        return char

def encrypt(text, key):
    # split the string into a list of characters and replace spaces with ||
    characters = [w.replace(' ', '||') for w in [char for char in text]]
    # encrypt the message and return it
    return ' '.join(map(str, [encryptChar(x, key) for x in characters]))

def decryptChar(char, key):
    # check if the character is a number
    if re.match('^[0-9]*$', char):
        # create a dictionary with all of the lower case letters
        d = dict(enumerate(string.ascii_lowercase, 1))
        # return the letter in the index of the resulting number
        return d[math.sqrt(int(char) - int(key))]
    # return || as a space
    if char == '||':
        return ' '
    # if the character is not a number or ||, just return it
    else: return char
        
        
def decrypt(text, key):
    # split the string into a list
    characters = text.split()
    # decrypt the message and return it
    return ''.join([decryptChar(x, key) for x in characters])

def menu():
    inp = input('Welcome to Enkodo!\nWhat would you like to do?\n\n1) Encrypt a message\n2) Decrypt a code\n3) Exit\nYour choice: ')

    if inp == '1':
        msg = input('\nPlease input the message you would like to encrypt:\n')
        key = input('\nPlease provide a key to encrypt that with.\n')
        encrypted = encrypt(msg, key)

        print('\nYour message has been successfully encrypted. Here it is!\n')
        print(encrypted)
        exit()
    if inp == '2':
        code = input('\nPlease input the code you would like to decrypt:\n')
        key = input('\nWhat was the key the code was encrypted with?\n')
        decrypted = decrypt(code, key)

        print('\nYour message has been successfully decrypted. Here it is!\n')
        print(decrypted)
        exit()
    if inp == '3':
        print('\nGoodbye!')
        exit()
    
menu()