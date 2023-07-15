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


title = input("Enter account title: ")
balance = int(input("Enter account balance: "))
interest_rate = int(input("Enter interest rate: "))

account = Account(title, balance)
account.deposit(5000)
print(account.get_balance())  
 

savings_account = SavingsAccount(title, balance, interest_rate)
interest_amount = savings_account.interest_amount()
print(interest_amount)
