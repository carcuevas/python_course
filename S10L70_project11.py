### Creating a BANK
## We will create 2 accounts, a current account and a savings account
# So we'll create an account parent class since both of them will have similar behaviour, deposit, withdraw money and print some statements
# Current account will have as limit 1000 EUR of negative for withdrawing and the saving accounts wont have any limit

# First the abstract class with the name/balance/min_balance, generally for every account
class Account:

    # the constructor
    def __init__(self, name, balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance



    # Method for doing deposit of the money into the accounts
    def deposit(self, amount):
        self.balance += amount # it's the same as writting self.balance = self.balance + amount


    # Method for withdraw money
    def withdraw(self,amount):

        if self.balance - amount >= self.min_balance:
            self.balance -= amount # it's the same as writting self.balance = self.balance + amount

        else:

            print("Sorry not enough funds")

    #Method for print statement of the account
    def statement(self):
        print("Account Balance: {}  Euros".format(self.balance))


    

## Now we have to create the class for current account inheriting from Account
class Current(Account):

    #The constructor, the parameters needed to create a current account
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000) ## We'll pass here the maximum negative amount for the current account
        
            
    # The class for showing the oject with some nice format 
    def __str__(self):
        return("{}'s Current Account -> Balance {} Euros".format(self.name, self.balance))




## Now we have to create the class for savings account inheriting from Account
class Sabings(Account):

    #The constructor, the parameters needed to create a current account
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0) ## We'll pass here the maximum negative as 0 because it's a savings account
        
            
    # The class for showing the oject with some nice format 
    def __str__(self):
        return("{}'s Savings Account -> Balance {} Euros".format(self.name, self.balance))



    
        
    
        
