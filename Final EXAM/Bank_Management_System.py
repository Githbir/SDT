#    *** Bank Management System ***

class Account:
    def __init__(self, name, email, address, account_Type):
        self.name = name
        self.email = email
        self.address = address
        self.account_Type = account_Type  # Saving & Current
        self.balance = 0
        self.account_number = name + email  # generated automatically
        self.transactions = []  # Store transaction history
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"{amount} Deposited Successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal Amount Exceeded.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print(f"{amount} Withdrawn Successfully.")

    def check_balance(self):
        print(f"Available Balance: {self.balance}")

    def transaction_history(self):
        if not self.transactions:
            print("No transactions Still.")
        else:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.transactions.append(f"Loan taken: {amount}")
            print(f"Loan of {amount} Successfully.")
        else:
            print("Loan Limit Exceeded.You can take at most two loans Already.")

    def transfer(self, recipient_account, amount):
        if amount > self.balance:
            print("Insufficient balance for the transfer.")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            self.transactions.append(f"Transferred {amount} to {
                                     recipient_account.account_number}")
            print(f"{amount} transferred to account number {
                  recipient_account.account_number} Successfully.")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.bank_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True
        self.bankrupt = False

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)

        self.accounts[account.account_number] = account
        print(f"Account created successfully with account number: {
              account.account_number}")
        return account

    def account_check(self, account_num):
        if account_num in self.accounts:
            return True
        else:
            print("Account not found.")
            return False

    def delete_account(self, account_number):
        del self.accounts[account_number]  # delete acount
        print(f"Account {account_number} deleted successfully.")

    def list_accounts(self):
        if not self.accounts:
            print("No Account Available.")
        else:
            print("List of all User Accounts:")
            for account_number, account in self.accounts.items():
                print(f"Account Number: {account_number}, Name: {
                      account.name}, Balance: {account.balance}")

    def check_total_balance(self):
        total_balance = sum(
            account.balance for account in self.accounts.values())
        print(f"Total balance in the bank: {total_balance}")

    def check_total_loans(self):
        total_loans = sum(
            account.loan_count for account in self.accounts.values())
        print(f"Total loans taken: {total_loans}")

    def enable_disable_loan_feature(self, status):
        self.loan_feature_enabled = status
        if status:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")

    def bankrupt_Notice(self):
        self.bankrupt = True


bank = Bank()

while 1:
    print(' ______________________________________ ')
    print('|                                      |')
    print('|       1 Admin                        |')
    print('|       2 User                         |')
    print('|       3 Exit                         |')
    print('|______________________________________|')

    op = int(input())

    if op == 1:  # Admin action
        print("Admin Menu:\n1.Create account\n2.Delete account\n3.List accounts")
        print("4.Total balance\n5.Total loans\n6.Enable/Disable loans\n7.Bankrupt Notice\n")
        admin_choice = int(input())

        if admin_choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)

        elif admin_choice == 2:
            account_num = (input("Enter account number to delete: "))
            if bank.account_check(account_num):
                bank.delete_account(account_num)

        elif admin_choice == 3:
            bank.list_accounts()

        elif admin_choice == 4:
            bank.check_total_balance()

        elif admin_choice == 5:
            bank.check_total_loans()

        elif admin_choice == 6:
            status = input("Enable loan feature? (yes/no): ").lower() == 'yes'
            bank.enable_disable_loan_feature(status)

        elif admin_choice == 7:
            bank.bankrupt_Notice()
            print("Now, Bank is bankrupt!!!!")

    elif op == 2:  # User actions
        print("User Menu:\n1.Create account\n2.Deposit\n3.Withdraw\n4.Check balance")
        print("5.Transaction history\n6.Take loan\n7.Transfer")
        user_choice = int(input())

        if user_choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            account = bank.create_account(name, email, address, account_type)

        elif user_choice == 2:
            account_num = (input("Enter your account number: "))
            if bank.account_check(account_num):
                amount = int(input("Enter deposit amount: "))
                bank.accounts[account_num].deposit(amount)

        elif user_choice == 3:
            if bank.bankrupt == False:
                account_num = (input("Enter your account number: "))
                if bank.account_check(account_num):
                    amount = int(input("Enter withdrawal amount: "))
                    bank.accounts[account_num].withdraw(amount)
            else:
                print("The bank is bankrupt. Now, Withdraw Not Possible")

        elif user_choice == 4:
            account_num = (input("Enter your account number: "))
            if bank.account_check(account_num):
                bank.accounts[account_num].check_balance()

        elif user_choice == 5:
            account_num = (input("Enter your account number: "))
            if bank.account_check(account_num):
                bank.accounts[account_num].transaction_history()

        elif user_choice == 6:
            account_num = (input("Enter your account number: "))
            if bank.account_check(account_num):
                amount = int(input("Enter loan amount: "))
                bank.accounts[account_num].take_loan(amount)

        elif user_choice == 7:
            if bank.bankrupt == False:
                from_account_num = (input("Enter your account number: "))

                if bank.account_check(from_account_num):
                    to_account_num = (
                        input("Enter recipient account number: "))

                    if bank.account_check(to_account_num):
                        amount = int(input("Enter transfer amount: "))
                        recipient = bank.accounts.get(to_account_num)
                        bank.accounts[from_account_num].transfer(
                            recipient, amount)
            else:
                print("The bank is bankrupt. Now, Transfer Not Possible")

    elif op == 3:
        break

print(' ======================================== ')
print('||       Bank Shut Down                 ||')
print(' ========================================')


# Testing

#  ______________________________________
# |                                      |
# |       1 Admin                        |
# |       2 User                         |
# |       3 Exit                         |
# |______________________________________|
# 1
# Admin Menu:
# 1.Create account
# 2.Delete account
# 3.List accounts
# 4.Total balance
# 5.Total loans
# 6.Enable/Disable loans
# 7.Bankrupt Notice

# 1
# Enter name: a
# Enter email: 1@
# Enter address: 1
# Enter account type (Savings/Current): s
# Account created successfully with account number: a_1@
#  ______________________________________
# |                                      |
# |       1 Admin                        |
# |       2 User                         |
# |       3 Exit                         |
# |______________________________________|
# 1
# Admin Menu:
# 1.Create account
# 2.Delete account
# 3.List accounts
# 4.Total balance
# 5.Total loans
# 6.Enable/Disable loans
# 7.Bankrupt Notice

# 1
# Enter name: b
# Enter email: 2@
# Enter address: b
# Enter account type (Savings/Current): c
# Account created successfully with account number: b_2@
#  ______________________________________
# |                                      |
# |       1 Admin                        |
# |       2 User                         |
# |       3 Exit                         |
# |______________________________________|
# 2
# User Menu:
# 1.Create account
# 2.Deposit
# 3.Withdraw
# 4.Check balance
# 5.Transaction history
# 6.Take loan
# 7.Transfer
# 1
# Enter name: c
# Enter email: 3@
# Enter address: c
# Enter account type (Savings/Current): s
# Account created successfully with account number: c_3@
#  ______________________________________
# |                                      |
# |       1 Admin                        |
# |       2 User                         |
# |       3 Exit                         |
# |______________________________________|
# 2
# User Menu:
# 1.Create account
# 2.Deposit
# 3.Withdraw
# 4.Check balance
# 5.Transaction history
# 6.Take loan
# 7.Transfer
# 1
# Enter name: d
# Enter email: 4@
# Enter address: d
# Enter account type (Savings/Current): c
# Account created successfully with account number: d_4@
#  ______________________________________
# |                                      |
# |       1 Admin                        |
# |       2 User                         |
# |       3 Exit                         |
# |______________________________________|
# 1
# Admin Menu:
# 1.Create account
# 2.Delete account
# 3.List accounts
# 4.Total balance
# 5.Total loans
# 6.Enable/Disable loans
# 7.Bankrupt Notice

# 3
# List of all User Accounts:
# Account Number: a_1@, Name: a, Balance: 0
# Account Number: b_2@, Name: b, Balance: 0
# Account Number: c_3@, Name: c, Balance: 0
# Account Number: d_4@, Name: d, Balance: 0
#  ______________________________________
# |                                      |
# |       1 Admin                        |
# |       2 User                         |
# |       3 Exit                         |
# |______________________________________|
# 3
#  ========================================
# ||       Bank Shut Down                 ||
#  ========================================
#
