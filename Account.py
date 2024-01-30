class Account():
    def __init__(self, name, balance, password) -> None:
        self.name = name
        self.balance = int(balance)
        self.password = password
        
    def deposit(self, amountToDeposit, password=input('')):
        if password != self.password:
            trails = 0
            limit = 3
            while trails < limit:
                print('sorry, incorrect password')
                trial = input('')
                trails += 1
                if trial == self.password:
                    print('you are correct')
                    break
            else:
                print('!!! sorry, number of trials exceeded. Please try again later')
            return None
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        self.balance = self.balance + amountToDeposit
        return self.balance
    
    def withdraw(self, amountToWithdraw, password=input('')):
        if password != self.password:
            trails = 0
            limit = 3
            while trails < limit:
                print('sorry, incorrect password')
                trial = input('')
                trails += 1
                if trial == self.password:
                    print('you are correct')
                    break
            else:
                print('!!! sorry, number of trials exceeded. Please try again later')
            return None
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        if amountToWithdraw > self.balance:
            print('You cannot wthdraw more than you have in your account')
            return None
        self.balance = self.balance - amountToWithdraw
        return self.balance
    
    def getBalance(self, password=input('')):
        if password != self.password:
            trails = 0
            limit = 3
            while trails < limit:
                print('sorry, incorrect password')
                trial = input('')
                trails += 1
                if trial == self.password:
                    print('you are correct')
                    break
            else:
                print('!!! sorry, number of trials exceeded. Please try again later')
            return None
        return self.balance
    
    def showInfo(self):
        print('      Name:', self.name)
        print('      Balancce:', self.balance)
        print('      password:', self.password)
        print()
        

oAccount = Account('Ayoola Balogun', 100000, 'splash')
newBalance = oAccount.deposit(20000)
#balance = oAccount.getBalance()
oAccount.showInfo()