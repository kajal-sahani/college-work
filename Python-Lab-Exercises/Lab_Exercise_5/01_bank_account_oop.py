"""
Lab Exercise 5 - Program 1
Bank Account System using OOP
Student: Kajal
"""

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")

    def display(self):
        print("\n----- Account Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("---------------------------")


print("=" * 45)
print("      BANK ACCOUNT SYSTEM (OOP)")
print("=" * 45)

# Create account
acc_no = input("\nEnter Account Number: ")
name = input("Enter Account Holder Name: ")
acc = BankAccount(acc_no, name)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        amt = float(input("Enter amount to deposit: "))
        acc.deposit(amt)
    elif choice == '2':
        amt = float(input("Enter amount to withdraw: "))
        acc.withdraw(amt)
    elif choice == '3':
        acc.display()
    elif choice == '4':
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice!")
