class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            raise ValueError('На счете недостаточно средств')
        else:
            self._balance -= amount

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)



# TEST_5:
account1 = BankAccount(balance=100)
account2 = BankAccount(balance=0)
account1.transfer(account2, 20)
print(account1.get_balance())
print(account2.get_balance())

# TEST_6:
account = BankAccount()
print(hasattr(account, '_balance'))

# TEST_7:
account = BankAccount(balance=10)
account.withdraw(10)
print(account.get_balance())

# TEST_8:
account1 = BankAccount(balance=100)
account2 = BankAccount()
account1.transfer(account2, 100)
print(account1.get_balance())
print(account2.get_balance())