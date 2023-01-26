from enum import Enum
from abc import ABC

CONFIRMATION_VALIDATOR = lambda x: x.lower() not in ['yes', 'y', 'no', 'n']

class AccountTypes(Enum):
    Current = 1
    Savings = 2

class Account(ABC):
    def __init__(self):
        self.__balance = 0

    def getBalance(self):
        return self.__balance

    def setBalance(self, newBalance):
        self.__balance = newBalance

class CurrentAccount(Account):
    pass

class SavingsAccount(Account):
    INTEREST_RATE = 0.02

    def __init__(self):
        super().__init__()

    def calculateInterest(self):
        return self.getBalance() * SavingsAccount.INTEREST_RATE

    def setBalance(self, newBalance):
        if newBalance < 0:
            raise ValueError('You can not have a negative balance!')
            
        return super().setBalance(newBalance)

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

    def accountType(self):
        if isinstance(self.__account, CurrentAccount):
            return AccountTypes.Current
        elif isinstance(self.__account, SavingsAccount):
            return AccountTypes.Savings

    def addInterest(self):
        if isinstance(self.__account, SavingsAccount):
            interest = self.__account.calculateInterest()
            self.__account.setBalance(self.fetchBalance() + interest)
            return interest
        else:
            return 0

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
    print(f"""Welcome to the bank! What would you like to do?

1) View your current balance
2) Pay in money
3) Withdraw money""" + ("""
4) Add interest""" if controller.accountType() == AccountTypes.Savings else ""))

    choice = fetchValue(int, 'integer', 'Please make your selection: ', lambda x: (x > 5 or x <= 0))

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
    elif accountType == AccountTypes.Savings and choice == 4:
        interest = controller.addInterest()
        print(f'Added £{interest:.2f} worth of interest!')
        displayBalance()


if __name__ == '__main__':
    print("""Please choose an account type:
1) Current Account
2) Savings Account""")
    accountType = AccountTypes.Savings if fetchValue(int, 'account type', 'Please select an account type (1-2): ', lambda x: (x < 1 or x > 2)) == 2 else AccountTypes.Current
    account = CurrentAccount() if accountType == AccountTypes.Current else SavingsAccount()
    controller = Controller(account)

    while True:
        menu()

        again = fetchValue(str, 'input', 'Would you like to go again? (y/n)', CONFIRMATION_VALIDATOR)

        if again in ['n', 'no']:
            break