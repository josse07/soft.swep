#Bank that manages a dictionary of account objects
from Account import *
class Bank():
    def __init__(self, hours, address, phone) -> None:
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone
    def askForValidAccounNumber(self):
        accountNumber = input('what is your account number: ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('There is no account '+ str(accountNumber))
        return accountNumber
    def getUserAccount(self):
        accountNumber = self.askForValidAccounNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidAccounNumber()
        return oAccount
    def createAccount(self, theName, theStartingAmount, thePassword, theAddress, theTelephone, theDateOfBirth):
        oAccount = NewAccountDetails(theName, theStartingAmount, thePassword, theAddress, theTelephone, theDateOfBirth)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        #increment to prepare fo next account to be created
        self.nextAccountNumber += 1
        return newAccountNumber
    def openAccount(self):
        print('*** Open Account ***')
        userName = input('what is the name for this account? ')
        userStartingAmount = input('what is the starting amount for this account? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('what is the password for this account? ')
        userAddress = input('Enter the address you want to use for this account? ')
        userTelephone = input('Enter the phone Number for this account ')
        userDateOfBirth = input('what is your date of birth for this account? ')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword, userAddress, userTelephone, userDateOfBirth)
        print('Your new account Number is: ', userAccountNumber)
        print()
    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = input('what is your account number? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('what is your password? ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print('You had ', theBalance, ' in your account, which is being returned to you')
            #remove user's account from the dictionary of accounts
            del self.accountsDict[userAccountNumber]
            print('your account is now closed.')
    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account Number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter your password: ')
        oAccount = self.accountsDict[userAccountNumber]
        
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your Balance is: ', theBalance)
    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUserAccount()
        depositAmount = input('please enter amount to deposit: ')
        userPassword = input('Please  enter the password for this account: ')
        theBalance = oAccount.deposit(depositAmount, userPassword)
        
        print('deposited: ', depositAmount)
        print('Your new balance is: ', theBalance)
    def showInfo(self):
        print('*** showInfo ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('     Account:', userAccountNumber)
            oAccount.showInfo()
            print()
    def getInfo(self):
        print('Hours: ', self.hours)
        print('Address: ', self.address)
        print('Phone: ', self.phone)
        print('we currently have ', len(self.accountsDict), ' account(s) open.')
        print()
    def withdraw(self):
        print('*** withdraw ***')
        oAccount = self.getUserAccount()
        userAmount = input('please enter amount to withdraw: ')
        userPassword = input('Please enter your password')
        theBalance = oAccount.withdraw(userAmount, userPassword)
        print('withdraw: ', userAmount)
        print('Your new balance is: ', theBalance)