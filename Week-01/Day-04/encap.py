class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance
