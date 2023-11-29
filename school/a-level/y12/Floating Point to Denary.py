import re

def twosComplementToDenary(bitPattern):
    value = 0

    for i in range(len(bitPattern) - 1, -1, -1):
        placeValue = 2 ** (len(bitPattern) - i - 1)
        if i == 0: placeValue *= -1

        value += int(bitPattern[i]) * placeValue

    return value

def twosComplementNormalisedToDenary(bitPattern):
    wholePart, fractionalPart = bitPattern[0], bitPattern[-len(bitPattern)+1:]
    value = -1 if int(wholePart) == 1 else 0

    for i in range(len(fractionalPart), 0, -1):
        placeValue = 2 ** -i
        value += int(fractionalPart[i - 1]) * placeValue

    return value

while True:
    try:
        binary = input('Please enter the bit pattern you would like to decode: ')

        if re.match('[^01]+', binary):
            raise ValueError

        break
    except ValueError:
        print('Please ensure that you input a valid binary sequence!')

while True:
    try:
        while True:
            try:
                mantissaBits = int(input('Please enter the amount of bits that the mantissa uses: '))
                break
            except ValueError:
                print('Please ensure that you input a valid integer!')

        while True:
            try:
                exponentBits = int(input('Please enter the amount of bits that the exponent uses: '))
                break
            except ValueError:
                print('Please ensure that you input a valid integer!')

        if exponentBits + mantissaBits != len(binary):
            raise ValueError

        break
    except ValueError:
        print(f'The amount of bits you inputed for the mantissa and exponent do not add up to the length of your sequence - please make sure they span the entire range of the sequence! For reference, your sequence was {binary}')

binary = str(binary)
mantissa = binary[:mantissaBits]
exponent = binary[-exponentBits:]

denaryExponent = twosComplementToDenary(exponent)
denaryMantissa = twosComplementNormalisedToDenary(mantissa)

print(denaryMantissa * (2 ** denaryExponent))