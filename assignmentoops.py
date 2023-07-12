class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title, balance=0, interest_rate=0):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

    def interest_amount(self):
        return self.balance * (self.interest_rate / 100)


account = Account("Ashish", 5000)
account.deposit(1000)
print(account.get_balance())  
account.withdrawal(500)
print(account.get_balance())  

savings_account = SavingsAccount("Ashish", 5000, 5)
interest_amount = savings_account.interest_amount()
print(interest_amount)  