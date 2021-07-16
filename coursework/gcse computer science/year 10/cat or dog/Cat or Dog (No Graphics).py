def catOrDog():
    global cat, dog
    got = input('Enter what type of pet you have')
    got = got.lower()

    if got == 'dog':
        dog = dog + 1
    elif got == 'cat':
        cat = cat + 1
    else:
        print('Only cats and dogs count.')

def printTotals():
    global cat, dog
    print('Total cats: {0}'.format(cat))
    print('Total dogs: {0}'.format(dog))

cat = 0
dog = 0

while True:
    catOrDog()
    printTotals()
    again = input('Again? y/n')
    if again == 'n':
        break