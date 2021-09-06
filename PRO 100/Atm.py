class Atm(object):
    def __init__(self, cashwithdrawal, balanceenquiry, cashdeposit) :
        self.cashwithdrawal=cashwithdrawal
        self.balanceenquiry=balanceenquiry
        self.cashdeposit=cashdeposit
       
    def withdraw(self):
        print("Cash Withdrawn")
    def enquiry(self):
        print("Getting Enquired")
    def deposit(self):
        print("Being Deposited")        
        

atm = Atm("2000","Processing","1000")

print(atm.color)  # prints black
atm.start() # executes themethod