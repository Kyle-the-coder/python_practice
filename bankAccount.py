

class BankAccount:
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.rate = int_rate
        self.balance = balance


        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        if(self.balance < 0):
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        # your code here
        print(self.balance)
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance *= self.rate
        return self 
        

        
        

new_account1 = BankAccount(.01, 1000)

new_account2 = BankAccount(.05, 20)


new_account1.deposit(1000).deposit(50).deposit(5).withdraw(1000).yield_interest().display_account_info()

new_account2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(5).withdraw(20).yield_interest()

