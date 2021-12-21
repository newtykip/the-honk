output = ''
asc = 0

msg = input('Please input the text.')
key = input('How many characters would you like to shift that text by?')

for i in msg:
    asc = ord(i)
    shiftChr = asc + int(key)
    output = output + chr(shiftChr)

print(output)