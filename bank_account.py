class BankAccount():
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited successfully")
        else:
            print("Deposit amount must be greater than zero")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")
        else:
            print("Withdraw amount must be greater than zero")

    def display_balance(self):
        print("Account No:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, balance):
        super().__init__(account_number, name, balance)

    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print("Interest added successfully")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, name, balance, overdraft_limit=5000):
        super().__init__(account_number, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= -self.overdraft_limit:
                self.balance -= amount
                print("Withdrawal successful")
            else:
                print("Withdrawal exceeds overdraft limit")
        else:
            print("Withdraw amount must be greater than zero")
        self.display_balance()

acc = SavingsAccount(101, "Archana", 1000)
acc.display_balance()
acc.deposit(2000)
acc.display_balance()
acc.withdraw(500)
acc.display_balance()
acc.add_interest()
acc.display_balance()

acc1 = CurrentAccount(102, "Archana", 1000)  
acc1.withdraw(3000)