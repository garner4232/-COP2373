# This program prompts the user for some bank information. The program then
# asks the user questions about withdrawing funds and depositing funds.
# Lastly, the program calculates the interest rate.

# if one of the question requires an integer, this function ensures it is an integer
def numberChecker(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.\n")


# This class is the bank account and has all of the functions needed to make it work
class BankAcct:
    # Initializes the variables that will be used
    def __init__(self, name, acctNumber, balance, interestRate):
        self.name = name
        self.acctNumber = acctNumber
        self.balance = balance
        self.interestRate = interestRate

    # if the user wants to, they can adjust the interest rate here
    def adjustInterest(self, newRate):
        self.interestRate = newRate
        print(f"Your interest rate has been adjusted to {newRate * 100:.2f}%\n")

    # The user can use this function to deposit money into their account
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"You deposited  ${amount:.2f}\n")
        else:
            print("Amount must be positive.\n")

    # The user can withdraw money using this function
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.\n")
        elif amount <= 0:
            print("Amount must be positive.\n")
        else:
            self.balance -= amount
            print(f"You withdrew ${amount:.2f}\n")

    # This function just returns the balance of the account to be used later
    def getBalance(self):
        return self.balance

    # Calculates the interest based on the day period given by the user
    def calculateInterest(self, days):
        interest = self.balance * self.interestRate * (days / 365)
        return interest

    # Returns everything to be printed out properly
    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acctNumber}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Interest Rate: {self.interestRate * 100:.2f}%\n")


# asks the user for the account details
def testAcct():
    name = input("Enter account holder's name; ")
    acctNumber = input("Enter account number; ")
    balance = numberChecker("Enter initial balance: ")
    interestRate = numberChecker("Enter annual interest rate (use decimals accurately): ")

    # creates the new bank account
    account = BankAcct(name, acctNumber, balance, interestRate)

    # Displays the initial account details.
    print("\nAccount Details:")
    print(account)

    # Asks the user for a deposit amount and then sends the amount to be processed.
    depositAmt = numberChecker("Enter amount to deposit: ")
    account.deposit(depositAmt)
    print("Account Details after deposit:")
    print(account)
    # Asks the user for a withdrawal amount and processes the withdrawal.
    withdrawAmt = numberChecker("Enter amount to withdraw: ")
    account.withdraw(withdrawAmt)
    print("Account Details after withdrawl:")
    print(account)

    # Checks if the user wants to adjust the interest rate.
    adjust = input("Would you like to adjust the interest rate? (yes/no): ").strip().lower()
    if adjust == "yes":
        newRate = numberChecker("Enter the new interest rate (use decimals accurately) ")
        account.adjustInterest(newRate)
        print("After adjusting interest rate:")
        print(account)

    # asks for the number of days to calculate interest and display the result.
    days = numberChecker("Enter number of days for interest calculation: ")
    interestAmount = account.calculateInterest(days)
    print(f"Interest earned in {days} days ${interestAmount:.2f}\n")


testAcct()

