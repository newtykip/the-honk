counter = 26
ciphertext = input('Please input some ciphertext to decrypt.')
ciphertext = ciphertext.upper()

while counter >= 0:
    outputWord = ''

    for i in ciphertext:
        asc = ord(i)
        shiftChr = asc + counter

        if shiftChr >= 90:
            shiftChr = (shiftChr-90)+64

        outputWord = outputWord + chr(shiftChr)

    print(outputWord)
    counter = counter - 1