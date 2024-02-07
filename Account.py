class AbortTransaction(Exception):
    pass
class Account():
    def __init__(self, name, balance, password) -> None:
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password
    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount
    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('incorrect password for this amount')
        
        
    def deposit(self, amountToDeposit, password):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance 
    
    def withdraw(self, amountToWithdraw, password):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('you cannot withdraw more than you have in your account')
        self.balance = self.balance - amountToWithdraw
        return self.balance
    
    def getBalance(self, password_check):
        if self.password == password_check:
            return self.balance
        
       
    def showInfo(self):
        print('      Name:', self.name)
        print('      Balancce:', self.balance)
        print('      password:', self.password)
        
        
class NewAccountDetails(Account):
    def __init__(self, name, balance, password, address, telephone_number, date_of_birth) -> None:
        super().__init__(name, balance, password)
        self.address = address
        self.telephone_number = telephone_number
        self.date_of_birth = date_of_birth
    def showInfo(self):
        print('      Name:', self.name)
        print('      Balancce:', self.balance)
        print('      password:', self.password)
        print('      address:', self.address)
        print('      telephoneNumber:', self.telephone_number)
        print('      dateOfBirth:', self.date_of_birth)
        

