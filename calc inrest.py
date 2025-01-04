class Clac:
    def __init__(self , amount , rate, time):
        self.amount = amount
        self.rate = rate        
        self.time = time
    
    def SimpleIntrest(self):
        return f" Simple Intrest is {(self.amount*self.rate*self.time)/100:.2f}"
    
    def CompoundIntrest(self):
        total_amount = self.amount * (1 + (self.rate/100)) ** self.time
        compound_interest = total_amount - self.amount
        return f"Compound Interest is {compound_interest:.2f}"
    
def value(amount, rate, time)-> float:
    intrest = Clac(amount,rate,time)
    print(intrest.SimpleIntrest())
    print(intrest.CompoundIntrest())

if __name__ == "__main__":
    amount = float(input("Amount for inrest : "))
    rate = float(input("Rate for intrst : "))
    time = float(input("time period for intrst : "))
    value(amount, rate, time)