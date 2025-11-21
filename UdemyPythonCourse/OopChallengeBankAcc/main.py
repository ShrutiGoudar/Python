from bank import *

def main() :
    acct1 = Account('Jose',100)
    print(acct1)
    print(acct1.owner)
    print(acct1.accbal)
    acct1.deposit(50)
    acct1.withdraw(75)
    acct1.withdraw(500)
    
    
    
if __name__ == "__main__":
    main()
