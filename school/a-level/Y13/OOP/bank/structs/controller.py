from typing import List
import account

class Controller:
    def __init__(self, *accounts: List["account.Account"]):
        self.__accounts = accounts