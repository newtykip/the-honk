from time import sleep

def clearTerminal():
    print('\n' * 25)

def findPrimes(upperBound: int):
    """
    Implementation of the Sieve of Eratosthenes.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    mask = [True for _ in range(upperBound)]
    primes = []

    mask[0] = False
    mask[1] = False

    for i in range(2, upperBound):
        if mask[i]:
            primes.append(i)

            j = 2 * i

            while j < upperBound:
                mask[j] = False
                j += i

    return primes

possiblePrimes = findPrimes(1_000_000)
inputtedPrimes = []

def askForPrime():
    global possiblePrimes, inputtedPrimes

    while True:
        try:
            value = int(input("Please enter a prime number to add to the list: "))

            if value > 999_999 or value < 0:
                raise ValueError('Please ensure you enter an integer at most 6 digits long!')
            elif value not in possiblePrimes:
                raise ValueError('That is not a prime number! Please try again.')
            elif value in inputtedPrimes:
                raise ValueError('You have already inputted that prime number! Please enter a different one.')

            return inputtedPrimes.append(value)
        except ValueError as e:
            if e.args[0].startswith("invalid literal"):
                print('Please enter a valid integer!')
            else:
                print(e)

if __name__ == "__main__":
    while True:
        print("""Welcome to the prime checker!
What would you like to do?

1) Add a number to the list
2) View the list of inputted primes
3) Exit
""")

        while True:
            try:
                choice = int(input("Please enter your choice: "))

                if choice not in [1, 2, 3]:
                    raise ValueError

                break
            except ValueError:
                print("Please enter a valid integer that is at most six digits long.")

        clearTerminal()

        if choice == 1:
            askForPrime()
        elif choice == 2:
            print(', '.join(map(lambda x: str(x), inputtedPrimes)))
            sleep(2.5)
        elif choice == 3:
            exit()

        clearTerminal()
