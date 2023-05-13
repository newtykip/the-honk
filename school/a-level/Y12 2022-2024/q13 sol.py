from random import choice

def randomDigit(dateOfBirth):
    return choice("".join(dateOfBirth.split("/")))

def getUsername(firstName, lastName, dateOfBirth):
    day, month, year = dateOfBirth.split("/")
    return f"{firstName[0:3]}{randomDigit(dateOfBirth)}{randomDigit(dateOfBirth)}{lastName[len(lastName)-3:len(lastName)]}{day}{month}{year[len(year)-2:len(year)]}"

print(getUsername("John", "Smith", "19/03/1989"))