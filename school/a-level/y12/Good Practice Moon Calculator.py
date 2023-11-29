from random import choice
from time import sleep

# https://www.funkidslive.com/learn/top-10-facts/top-10-facts-about-the-moon/
MOON_FACTS = [
    'The moon is the Earth\'s only natural satellite',
    'It takes 27.3 days for the Moon to travel all the way around the Earth',
    'The Moon is a lot smaller than The Sun',
    'The Moon was made when a rock smashed into the Earth',
    'The Moon controls the tides',
    'There is water on the Moon',
    'Earth\'s Moon is the only place beyond Earth where humans have set foot',
    'You can\'t breathe on the Moon',
    'The Moon is getting further away',
    'The Moon ISN\'T made of cheese'
]

weight = None # measured in kg

# Determine the user's weight
def updateWeight():
    global weight
    
    while True:
        try:
            weight = float(input("Please enter your weight in kilograms: "))
            break
        except ValueError:
            print("Please make sure you enter a valid number!")

# Calculate the user's moon weight
def computeMoonWeight(kg):
    return kg * 0.165

def clearTerminal():
    print('\n' * 20)

if __name__ == "__main__":
    updateWeight()

    # Menu
    while True:
        clearTerminal()
        print("""Welcome to the moon calculator! Please select an option:
1) Find out your moon weight!
2) Find out your moon weight for the next 10 years!
3) Change your weight!
4) Find out a moon fact!
5) Quit the program
""")

        userSelection = None

        # Determine the user's choice
        while True:
            try:
                userSelection = int(input("Choice (1-5): "))

                if userSelection > 5 or userSelection < 1:
                    raise ValueError
                
                break
            except ValueError:
                print("Please enter the number associated with a valid choice!")

        clearTerminal()

        if userSelection == 1:
            moonWeight = computeMoonWeight(weight)
            print(f'Your moon weight would be {moonWeight:.2f}kg!')

        elif userSelection == 2:
            print('Your moon weight for the next 10 years is as follows:')

            moonWeight = computeMoonWeight(weight)
            print(f'Present: {moonWeight:.2f} kg')

            for i in range(1, 11):
                moonWeight = computeMoonWeight(weight + i)
                print(f'Year {i}: {moonWeight:.2f} kg')

        elif userSelection == 3:
            updateWeight()
            continue

        elif userSelection == 4:
            fact = choice(MOON_FACTS)
            print('Fun Fact!')
            print(f'{fact}!')

        elif userSelection == 5:
            exit()

        sleep(2.5)