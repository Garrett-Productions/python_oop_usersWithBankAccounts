class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance=0 ): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):                  #increases the account balance by the given amount
        self.balance += amount
        return self


    def withdraw(self, amount): #decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if self.balance < amount:
            print("Insufficient Funds")
            self.balance -= 5
        else:
            self.balance -= amount
            return self


    def display_account_info(self):
        print(f"Your Balance:${self.balance}.") #This is an F statement printing the current balance.
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
        else:
            print("Sorry buddy your account needs to be above 0.")
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

# savingsAccount = BankAccount(.05, 4200) 
# checkingAccount = BankAccount(.07, 10540)

# checkingAccount.deposit(1950).deposit(4200).withdraw(800).withdraw(300).yield_interest()

BankAccount.print_all_accounts()
print(BankAccount.print_all_accounts())

#We used default parameters above in line 4.

#We interact with this new attribute just as we do with previous attributes--the only difference is that we have personally defined the functionality of this class! 
#We know the attributes and methods available to the "account" attribute by looking at our BankAccount class.
#For example, from the User class we should be able to deposit money into the user's account:

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.class_BankAccount={"Checking":BankAccount(int_rate=0.04, balance=0), "Savings":BankAccount(int_rate=0.01, balance=0)}


    def make_deposit(self, amount, accountName):  #this method mirrors, for ex, the deposit method we created in our BankAccount class. But we call on BankAccount to do most the work
        self.class_BankAccount[accountName].deposit(amount) #this is similar to how id write out it out in my conditionals.
        self.display_user_balance(accountName)
        return self

    def make_withdrawal(self, amount, accountName):
        self.class_BankAccount[accountName].withdraw(amount)
        self.display_user_balance(accountName)
        return self

    def display_user_balance(self, accountName):
        self.class_BankAccount[accountName]
        print(f"Your {accountName} is:${self.class_BankAccount[accountName].balance}.")
        return self

    def transfer_money(self, amount, other_user, accountName):
        self.make_withdrawal(amount, accountName)
        other_user.make_deposit(amount, accountName)
        return self



garrett = User('garrett', 'garrett@gmail.com')
garrett.make_deposit(1000, "Checking").make_deposit(1500, "Savings").make_withdrawal(1500, "Savings")

matt = User('Matt', 'mattwehner32@gmail.com' )
matt.make_deposit(20000, "Checking").make_deposit(80000, "Savings").make_withdrawal(50000, "Savings")

matt.transfer_money(1000, garrett, 'Checking')
matt.display_user_balance('Checking')
garrett.display_user_balance('Checking')

#Thought Process as I go along

#thought process behind having the user access multiple accounts

#im thinkin ive linked the account with my self.class_BankAccount and made 2 seperate accounts for each user through building a dictionary. 
#to create interconnectivity to my classes in my User __init__ I added a connection to my class BankAccount through making a dicitonary of 2 keys of checking & savings both w a value of bankaccount
#in order for my user to choose with account they want to access, I need to create a variable in my methods allowing the user to choose, I chose [accountName] because it's a dictionary
#so in all my 'user' methods I need to allow my user to input which account they want to work with by inputting which accountName.
#I do this by calling my attribute "self.class_BankAccount" and then specifying which account, and because its a dictionary we use []..[accountName]

#thought process behind transferring money between users

# I have a method in my class User called transfer_money with parameters of (self, amount, accountName, other_user)
# I believe I can use the make deposit and make withdrawal methods already created to make this transfer magic happen
