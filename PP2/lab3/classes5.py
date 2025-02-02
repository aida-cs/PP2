class Account:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, Balance: {self.balance}")

ac = Account("John", 100)
ac.deposit(50)
ac.withdraw(200) 