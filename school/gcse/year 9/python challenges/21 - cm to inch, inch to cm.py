def cmToInch(cm):
    return str(cm * 0.393700787) + ' inches'

def inchToCm(inch):
    return str(inch * 2.54) + ' cm'

num = int(input('Please input a number.'))
unit = int(input('Would you like to...\n\n1) Convert from centimetres to inches\n2) Convert from inches to centimetres'))

# cm to inch
if unit == 1:
    print(cmToInch(num))
# inch to cm
elif unit == 2:
    print(inchToCm(num))
else:
    print('Invalid input.')
    exit()