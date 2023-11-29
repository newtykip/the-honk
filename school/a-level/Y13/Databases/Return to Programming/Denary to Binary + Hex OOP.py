from string import ascii_uppercase
from math import ceil
from timeit import timeit

BIT_COUNT = 8

class CustomError(Exception):
    pass

def nibble(value: int, k: int) -> int:
    """Gets the kth nibble from the value"""
    return (value >> (4 * k)) & 0b1111

class Converter:
    def __init__(self, bit_count: int, value: int):
        """The converter can change a denary value into a binary or hexadecimal string"""
        self.__bit_count = bit_count
        self.__value = value

    def update_value(self, value: int):
        """Update the current value stored in the converter"""
        self.__value = value

    def bin_str(self) -> str:
        """Output the value stored in the converter as a binary string"""
        binary = ""
        value = self.__value

        for i in range(self.__bit_count - 1, -1, -1):
            place_value = 2 ** i

            if value - place_value >= 0:
                binary += "1"
                value -= place_value
            else:
                binary += "0"

        return binary

    def hex_str(self) -> str:
        """Output the value stored in the converter as a hexadecimal string"""
        hexadecimal = ""
        nibble_count = ceil(self.__bit_count / 4)

        for k in range(nibble_count - 1, -1, -1):
            value = nibble(self.__value, k)
            i = value - 10

            if i >= 0:
                hexadecimal += ascii_uppercase[i]
            else:
                hexadecimal += str(value)

        return hexadecimal

    def __str__(self) -> str:
        return f"""Denary: {self.__value}
Binary: {self.bin_str()}
Hexadecimal: {self.hex_str()}"""

if __name__ == "__main__":
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

    # instantiate the converter
    converter = Converter(BIT_COUNT, denary)

    assert int(converter.bin_str(), 2) == denary
    assert int(converter.hex_str(), 16) == denary

    # output
    print(f"\n{converter}")

    # output times
    bin_time = timeit(lambda: converter.bin_str(), number=100000)
    hex_time = timeit(lambda: converter.hex_str(), number=100000)

    print(f"""
(100,000 trials)
Binary Conversion: {bin_time}
Hexadecimal Conversion: {hex_time}""")
