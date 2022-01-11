def linearSearch(data, value):
    for i in range(0, len(data)):
        if data[i] == value:
            return i
    return -1

class ConfirmationError(Exception):
    pass

numbers = []
addingStage = True

while addingStage:
    try:
        number = float(input('Please enter a number to add to the list'))
        numbers.append(number)
        while True:
            try:
                toContinue = input('Would you like to enter another number? (y/n)')
                if toContinue == 'y':
                    break
                if toContinue == 'n':
                    addingStage = False
                    break
                else:
                    raise ConfirmationError
            except ConfirmationError:
                print('Please make sure you enter a valid confirmation value!')
    except ValueError:
        print('Please make sure you enter a valid number!')

while True:
    try:
        toSearch = float(input('Please enter a number to find the index of'))
        index = linearSearch(numbers, toSearch)
        print(numbers)
        if index == -1:
            print('%.2f is not in the list' % (toSearch))
        else:
            print('%.2f is at index %i in the list' % (toSearch, index))
        break
    except ValueError:
        print('Please make sure you enter a valid number!')