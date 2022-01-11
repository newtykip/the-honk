import csv
import os

path = '%s\league-table.csv' % (os.getcwd())

def clear():
    print('\n' * 50)

def resolveDataType(data):
    result = data
    try:
        result = int(data)
    except ValueError:
        try:
            result = float(data)
        except ValueError:
            temp = list(data)
            if len(temp) > 0:
                i = 0
                for value in temp:
                    temp[i] = resolveDataType(value)
                    i += 1
            if len(temp) > 1:
                result = temp
    return result

def ensureFileExists():
    doesExist = os.path.isfile(path)

    if not doesExist:
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Games Played', 'Games Won', 'Games Lost', 'Games Drawn', 'Overall Points', 'GD'])
            file.close()

def readTeams():
    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader) # get the headers and remove them from the reader

        for row in reader:
            col = 0
            for value in row:
                print('%s: %s' % (headers[col], value))
                col += 1

        file.close()

def writeTeam():
    with open(path, 'r+') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = []

        for header in headers:
            response = input('%s?' % (header))
            data.append(response)

        writer = csv.writer(file)
        writer.writerow(data)
        file.close()

# Menu
def displayMenu():
    print("""Welcome to the League Table! What would you like to do?

1) View the current state of the League Table
2) Write to the League Table
3) Remove from the League Table""")

    while True:
        try:
            menuOption = int(input('Which option would you like to select? '))
            break
        except ValueError:
            print('Please make sure that your input is a valid integer!')
            continue

    if menuOption == 1:
        clear()
        readTeams()
    elif menuOption == 2:
        clear()
        writeTeam()

##ensureFileExists()
##displayMenu()
print(resolveDataType('[1,2,3]'))