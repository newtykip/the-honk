from random import randint

class Dice:
    def __init__(self, sides: int = 6):
        self.__sides = sides

    def roll(self):
        return randint(1, self.__sides)

DICE_COUNT = 2
DICE_SIDES = 6
ROLL_COUNT = 1000
FORMAT_STRING = '  {: ^10}  |  {: ^10}  |  {: ^10}'

dice = Dice(DICE_SIDES)
frequencies = {}

for _ in range(ROLL_COUNT):
    totalRoll = 0

    for _ in range(DICE_COUNT):
        totalRoll += dice.roll()

    key = f'{totalRoll}'

    if key in frequencies:
        frequencies[key] += 1
    else:
        frequencies[key] = 1

header = FORMAT_STRING.format('Dice Value', 'Frequency', 'Percentage')
print(f'Rolling {DICE_COUNT} dice ({DICE_SIDES} sided) {ROLL_COUNT} times...\n')
print(header)
print('-' * (len(header) + 3))

frequencies = sorted(frequencies.items(), key=lambda k:int(k[0]))

for value, frequency in frequencies:
    percentage = (frequency * 100) / ROLL_COUNT
    print(FORMAT_STRING.format(value, frequency, f'{percentage:.2f}%'))