BankAccount → Base class with
account_number, name, balance
Methods: deposit(), withdraw(), display_balance()
SavingsAccount → Subclass of BankAccount
Extra method add_interest() → adds 5% interest to balance
CurrentAccount → Subclass of BankAccount
Has overdraft_limit (default 5000)
Allows withdrawal even if balance is not enough, within overdraft limit

Program shows how to:
Deposit money
Withdraw money
Add interest (savings)
Use overdraft (current)
Display balance
