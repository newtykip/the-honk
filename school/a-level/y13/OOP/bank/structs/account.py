class Account:
    def __init__(self, initial_balance: float, overdraft: bool = False):
        self.__balance = initial_balance
        self.__overdraft = overdraft

    def set_overdraft(self, state: bool) -> bool:
        if self.__balance < 0:
            return False

        self.__overdraft = state
        return True

    def deposit(self, amount: float):
        self += amount

    def __add__(self, amount: float):
        self.__balance += amount

    def __iadd__(self, amount: float) -> "Account":
        self.__add__(amount)
        return self

    def withdraw(self, amount: float) -> bool:
        if amount > self.__balance and not self.__overdraft:
            return False

        self -= amount
        return True
    
    def __sub__(self, amount: float):
        new_value = self.__balance - amount

        if new_value < 0 and self.__overdraft or new_value >= 0:
            self.__balance = new_value

    def __isub__(self, amount: float) -> "Account":
        self.__sub__(amount)
        return self

    def __str__(self) -> str:
        return f"""Balance: {self.__balance}
Overdraft is {"enabled" if self.__overdraft else "disabled"}"""