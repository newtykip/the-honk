from string import ascii_uppercase
from math import ceil

BIT_COUNT = 8

class CustomError(Exception):
    pass

# get a number
max_value = 2 ** BIT_COUNT - 1

while True:
    try:
        denary = int(input(f"Please enter an integer (<={max_value}): "))

        if denary > max_value:
            raise CustomError(f"Please enter a valid integer (<={max_value})")
        elif denary < 0:
            raise CustomError("Please enter a valid integer (>=0)")

        break
    except ValueError:
        print("Please enter a valid integer")
    except CustomError as err:
        print(err)

# convert to binary
binary = ""
bin_number = denary

for i in range(BIT_COUNT - 1, -1, -1):
    value = 2 ** i

    if bin_number - value >= 0:
        binary += "1"
        bin_number -= value
    else:
        binary += "0"

assert int(binary, 2) == denary

# convert to hexadecimal
hexadecimal = ""
nibble_count = ceil(BIT_COUNT / 4)
nibbles = [binary[::-1][(4 * i):(4 * (i + 1))][::-1] for i in range(nibble_count)]
nibbles.reverse()

for nibble in nibbles:
    value = int(nibble, 2)
    i = value - 10

    if i >= 0:
        hexadecimal += ascii_uppercase[i]
    else:
        hexadecimal += str(value)

print(hexadecimal)

assert int(hexadecimal, 16) == denary

print(f"""
Denary: {denary}
Binary: {binary}
Hexadecimal: {hexadecimal}""")