class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = str(account_number)
        self.account_balance = float(account_balance)
        self.account_holder = str(account_holder)

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: Ksh{amount}. New balance: Ksh{self.account_balance}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: Ksh{amount}. New balance: Ksh{self.account_balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        return self.account_balance

# Create instance "my_account"
my_account = Account("11111", 10000.0, "Robert")

# Perform operations
my_account.deposit(5000.0)
my_account.withdraw(2000.0)
print(f"Final Balance for {my_account.account_holder}: Ksh{my_account.check_balance()}")

# Testing with multiple instances
account2 = Account("22222", 500.0, "Brian")
account2.withdraw(1000.0)  # Should fail due to insufficient funds
account2.deposit(1000.0)
print(f"Account 2 Balance: Ksh{account2.check_balance()}")
