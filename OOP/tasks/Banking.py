class Account:
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print(amount, 'is debited from your Accounts')
        print('Remaining Balance is : ',self.getBalance())

    def credit(self, amount):
        self.balance += amount
        print(amount, 'is credited to your Accounts')
        print('Remaining Balance is : ',self.getBalance())

    def getBalance(self):
        return self.balance

account1 = Account(1234,4000)

# expenese 
account1.debit(500)

# profit 
account1.credit(30000)

# Account 2 

account2 = Account(22334,2000)
# profit 
account2.credit(40000)


