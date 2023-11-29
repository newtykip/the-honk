def happyCheck(number: int):
    seen = set()

    while number > 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in list(str(number)))
        
    return number == 1

print(happyCheck(19))