class bankAccount:
    def __init__(self,accountholder,balance=0):
        self.accountholder = accountholder
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount} add to the account. and new balance is{self.balance}")

    def withdraw(self, amount):
        if amount<self.balance:
            self.balance = self.balance-amount
            print(f"{amount} withdrwa and the new balance {self.balance}")

    def checkBalance(self):
        print(f"your current balance is {self.balance}")

    



c1 = bankAccount("Hassan", 890)
c1.checkBalance()
c2 = bankAccount("moeed", 8789)
c2.deposit(500)