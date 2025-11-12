class Account():
    #Note : Every class needs init and str. there are other methods. explore as per need
    def __init__(self, owner, balance):
        self.owner = owner
        self.accbal = balance
    
    def __str__(self):
        return f"Account owner : {self.owner}\nAccount Balance : {self.accbal}"
    
    def deposit(self, amount):
        self.accbal += amount
        print(f"Your new balance is {self.accbal}")
    
    def withdraw(self, amount):
        if self.accbal == 0 :
            print(f"Zero balance!! cannot withdraw")
        elif self.accbal < amount:
            print(f"Your current balance is {self.accbal}, cannot withdraw {amount}.")
        else :
            self.accbal -= amount
            print((f"Witdrew {amount}, new balance = {self.accbal}"))
    
    