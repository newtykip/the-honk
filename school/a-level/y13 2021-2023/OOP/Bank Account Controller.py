CONFIRMATION_VALIDATOR = lambda x: x.lower() not in ['yes', 'y', 'no', 'n']

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def getBalance(self):
        return self.__balance

    def setBalance(self, newBalance):
        self.__balance = newBalance

class Controller:
    OVERDRAWN_FEE = 5

    def __init__(self, account):
        self.__account = account

    def __overdrawnFee(self):
        balance = self.fetchBalance()

        if balance < 0:
            self.__account.setBalance(balance - Controller.OVERDRAWN_FEE)

        return balance < 0

    def fetchBalance(self):
        return self.__account.getBalance()

    def formatBalance(self):
        balance = self.fetchBalance()
        sign = '' if balance >= 0 else '-'
        return f'{sign}£{abs(balance):.2f}'

    def payIn(self, amount):
        self.__account.setBalance(self.fetchBalance() + amount)

    def withdraw(self, amount):
        fee = self.__overdrawnFee()
        self.__account.setBalance(self.fetchBalance() - amount)
        return fee

account = BankAccount()
controller = Controller(account)

def fetchValue(caster, typeName, prompt, validator = None, validatorFailMessage = None):
    while True:
        try:
            value = caster(input(prompt))

            if validator:
                if validator(value):
                    raise ValueError('validator')

            return value
        except ValueError as e:
            if str(e) == 'validator' and validatorFailMessage:
                print(validatorFailMessage)
            else:
                print(f'Please make sure you input a valid {typeName}.')

def displayBalance():
    print(f'You currently have a balance of {controller.formatBalance()}!')

def menu():
    print("""Welcome to the bank! What would you like to do?

1) View your current balance
2) Pay in money
3) Withdraw money
4) Exit""")

    choice = fetchValue(int, 'integer', 'Please make your selection: ', lambda x: (x > 4 or x <= 0))

    if choice == 1:
        displayBalance()
    elif choice == 2:
        value = fetchValue(float, 'float', 'Please enter the amount of money you would like to pay in: ')
        controller.payIn(value)
        displayBalance()
    elif choice == 3:
        value = fetchValue(float, 'float', 'Please enter the amount of money you would like to withdraw: ')
        chargedFee = controller.withdraw(value)

        if chargedFee:
            print(f'You are currently overdrawn! If you go through with this transaction, you will have to pay a fee of £{Controller.OVERDRAWN_FEE:.2f}, and your balance will become {controller.formatBalance()}.')
            confirm = fetchValue(str, 'input', 'Would you like to proceed? (y/n)', CONFIRMATION_VALIDATOR)

            if confirm in ['n', 'no']:
                controller.payIn(value + Controller.OVERDRAWN_FEE)
                print('Your transaction has been cancelled!')
            else:
                displayBalance()
        else:
            displayBalance()
    elif choice == 4:
        exit()


if __name__ == '__main__':
    while True:
        menu()

        again = fetchValue(str, 'input', 'Would you like to go again? (y/n)', CONFIRMATION_VALIDATOR)

        if again in ['n', 'no']:
            break