class BankAccount:
    def __init__(self, balance):
        # private variable
        self.__balance = balance

    # getter method (to read balance)
    def get_balance(self):
        return self.__balance

    # setter method (to update balance safely)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw amount")

# Using the class
account = BankAccount(1000)

# Direct access (not allowed)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(2000)
