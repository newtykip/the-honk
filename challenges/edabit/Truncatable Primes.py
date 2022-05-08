import math

class InputNotPrime(Exception):
    pass

def isPrime(number):
    if number % 2 == 0 or type(math.sqrt(number)) != float:
        return False

    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True

def isTruncatablePrime(number):
    if '0' in str(number):
        return False

    isRight = isRightTruncatablePrime(number)
    isLeft = isLeftTruncatablePrime(number)

    if isRight and isLeft:
        return 'both'
    elif isRight:
        return 'right'
    elif isLeft:
        return 'left'
    else:
        return False

def isRightTruncatablePrime(number):
    numbers = ['']

    for digit in reversed(list(str(number))):
        numbers.append(digit + numbers[len(numbers) - 1])
    numbers.remove('')

    for number in numbers:
        if not isPrime(int(number)):
            return False
    return True

def isLeftTruncatablePrime(number):
    numbers = ['']

    for digit in list(str(number)):
        numbers.append(numbers[len(numbers) - 1] + digit)
    numbers.remove('')

    for number in numbers:
        if not isPrime(int(number)):
            return False
    return True

while True:
    try:
        n = int(input("Please enter a prime number: "))
        if not isPrime(n):
            raise InputNotPrime
        break
    except ValueError:
        print('Please make sure your input is an integer!')
    except InputNotPrime:
        print('Please make sure your input is prime!')

print(isTruncatablePrime(n))
