import math

class CashRegister:
    __coins = {
        50: 0,
        20: 0,
        10: 0,
        5: 1,
        2: 0,
        1: 5,
        0.5: 2,
        0.2: 10,
        0.1: 10,
        0.05: 10,
        0.02: 5,
        0.01: 2
    }

    def checkout(self, cost, payment):
        totalPayment = 0

        # Add the money to the cash register and compute total payment
        for coinType in payment:
            self.__coins[coinType] += payment[coinType]
            totalPayment += payment[coinType] * coinType

        changeValue = totalPayment - cost
        change = {}

        for coinType in self.__coins:
            # Set an initial value for the change
            if changeValue - coinType >= 0:
                change[coinType] = 0

            # Keep attempting to provide change from the tray until we overpay
            while changeValue - coinType >= 0:
                changeValue -= coinType
                changeValue = round(changeValue, 2)
                self.__coins[coinType] -= 1
                change[coinType] += 1
            
        return change

register = CashRegister()

print(
    register.checkout(5.99, {
        10: 1
    })
)
