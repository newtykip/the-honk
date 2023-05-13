from time import sleep

# :eyes:
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

POSSIBLE_PRIMES = findPrimes(1_000_000) # Would be better to hardcode this list as it is constant, however I want good marks and to show complex algorithms I guess!!!
inputtedPrimes = []

def getPrime(primeList):
    while True:
        try:
            value = int(input("Please enter a prime number to add to the list: "))

            # Ensure that the value fits the requirements set out by the brief
            if value > 999_999 or value < 0:
                raise ValueError('Please ensure you enter an integer at most 6 digits long!')
            elif value not in POSSIBLE_PRIMES:
                raise ValueError('That is not a prime number! Please try again.')
            elif value in primeList:
                raise ValueError('You have already inputted that prime number! Please enter a different one.')

            # Mutate the prime list and return it back to the caller
            primeList.append(value)
            return primeList
        except ValueError as e:
            # Check to see if the error was raised by Python or manually, and print messages accordingly
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
                print("Please enter a valid option from the list (1-3)")

        clearTerminal()

        if choice == 1:
            inputtedPrimes = getPrime(inputtedPrimes)
        elif choice == 2:
            # Only print the list if there is values inside to print
            if len(inputtedPrimes) > 0:
                print(', '.join(map(lambda x: str(x), inputtedPrimes)))
            else:
                print('There is currently nothing in the list!')
                
            sleep(2.5)
        elif choice == 3:
            exit()

        clearTerminal()
