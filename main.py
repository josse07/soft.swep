#main program for controlling a Bank made up of accounts
#Bring in all the code of the Bank class
from test3 import *
#create an instance of the Bank
oBank = Bank(input('enter the hours: '), input('enter the address: '), input('enter the phone number: '))
#main code
#create two test accounts
joesAccountNumber = oBank.createAccount('joe', 200000, input('Enter your password '), input('Enter address: '), '090384783838', '2004-08-27')
print("Joes's account number is: ", joesAccountNumber)
marysAccountNumber = oBank.createAccount('Mary', 100000, input('Enter your password '), input('Enter your address '), '08034747636', '2005-07-06')
print("Mary's account Number is: ", marysAccountNumber)
print()
while True:
    print()
    print('To get an amount Balance, Press b')
    print('To close an account, Press c')
    print('To make a deposit, Press d')
    print('To get bank informaton, Press i')
    print('To open a new account, Press o')
    print('To quit, Press q')
    print('To show all accounts information, Press s')
    print('To make a Withdrawal, Press w')
    print()
    action = input('what do you want to do? ')
    action = action.lower()
    action = action[0]# grab the first letter
    print()
    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'o':
            oBank.openAccount()
        elif action == 's':
            oBank.showInfo()
        elif action == 'q':
            break
        elif action == 'w':
            oBank.withdraw()
        elif action == 'i':
            oBank.getInfo()

    except AbortTransaction as error:
        print('Sorry, that was not a valid action. Please try again')
print('DONE')