import math
import uuid
from datetime import datetime

class NegativeError(Exception):
    pass

def estimateTextFileSize(characterCount, bitsPerCharacter):
    return characterCount * bitsPerCharacter

def estimatePictureFileSize(width, height, colourDepth):
    return colourDepth * width * height

def estimateSoundFileSize(sampleRate, bitDepth, duration, channelCount):
    return sampleRate * duration * bitDepth * channelCount

def formatBits(bits):
    units = ['bits', 'bytes', 'kilobytes', 'megabytes', 'gigabytes', 'terrabytes', 'petabytes']

    for unit in units:
        if unit == units[0]:
            bits /= 8
        elif bits < 1024 or unit == units[len(units) - 1]:
            break
        else:
            bits /= 1024

    return '%i %s' % (math.floor(bits), unit)

def validateInput(function, inputMessage, errorMessage):
    while True:
        try:
            out = function(input(inputMessage))

            if (function == int or function == float) and out < 0:
                raise NegativeError

            break
        except ValueError:
            print(errorMessage)
            continue
        except NegativeError:
            print('The value you input can not be a negative number! Please try again (:')
            continue
    return out

def saveFile(data, fileType, bits):
    while True:
        toSave = input('Would you like to save your file? y/n').lower()

        if toSave == 'y':
            id = uuid.uuid1()
            file = open('%s.txt' % (id), 'w')
            file.write('Date: %s\n' % (datetime.now().strftime('%d/%m/%Y, %I:%M %p')))
            file.write('ID: %s\n' % (id))

            for set in data:
                key = set[0]
                value = set[1]
                file.write('%s: %s\n' % (key, value))

            file.write('---------------------------------------------\n\n')
            file.write('Your %s file\'s size is approximately %s' % (fileType, formatBits(bits)))
        break

# Menu
while True:
    print("""Welcome to the File Size Estimator! Please choose a function below:

1) Estimate Text File Size
2) Estimate Picture File Size
3) Estimate Sound File Size
""")

    choice = validateInput(int, 'Please make your choice: ', 'Please make sure you select a valid function!')

    if choice == 1:
        characterCount = validateInput(int, 'How many characters are in your text file? ', 'Please make sure you enter a valid integer!')
        bitsPerCharacter = validateInput(int, 'How many bits are used to store a character in your text file? ', 'Please make sure you enter a valid integer!')
        bits = estimateTextFileSize(characterCount, bitsPerCharacter)

        print('Your text file\'s size is approximately %s' % (formatBits(bits)))
        saveFile([['Character Count', characterCount], ['Bits Per Character', bitsPerCharacter]], 'text', bits)
    elif choice == 2:
        width = validateInput(float, 'What is the width of your image? ', 'Please make sure you enter a valid number!')
        height = validateInput(float, 'What is the height of your image? ', 'Please make sure you enter a valid number!')
        colourDepth = validateInput(int, 'What is the colour depth of your image? ', 'Please make sure you enter a valid integer!')
        bits = estimatePictureFileSize(width, height, colourDepth)

        print('Your image file\'s size is approximately %s' % (formatBits(bits)))
        saveFile([['Image Width', width], ['Image Height', height], ['Colour Depth', colourDepth]], 'image', bits)
    elif choice == 3:
        sampleRate = validateInput(int, 'What is the sample rate of your audio file? ', 'Please make sure you enter a valid integer!')
        bitDepth = validateInput(int, 'What is the bit depth of your audio file? ', 'Please make sure you enter a valid integer!')
        duration = validateInput(float, 'What is the duration of your audio file in seconds? ', 'Please make sure you enter a valid number!')
        channelCount = validateInput(int, 'How many channels does your audio file have? ', 'Please make sure you enter a valid integer!')
        bits = estimateSoundFileSize(sampleRate, bitDepth, duration, channelCount)

        print('Your audio file\'s size is approximately %s' % (formatBits(bits)))
        saveFile([['Sample Rate', sampleRate], ['Bit Depth', bitDepth], ['Duration', duration], ['Channel Count', channelCount]], 'text', bits)
    else:
        continue

    while True:
        again = input('Would you like to go again? y/n').lower()

        if again != 'y' and again != 'n':
            continue
        else:
            break

    if choice == 'y':
        continue
    else:
        break