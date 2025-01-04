class Calc:
    def __init__(self,num1 : int,num2 : int):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def extrect(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"
    
    def multi(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"
    
    def divide(self):
        if self.num1 < self.num2 or self.num1 == 0 or self.num2 == 0:
            return f"{self.num1} / {self.num2} = it not possible"
        else:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"

            

def ask(num1, num2,choise):
    calc = Calc(num1,num2)
    if choise == 1 :
        return calc.add()

    elif choise == 2 :
        return calc.extrect() 
    
    elif  choise == 3 :
        return calc.multi()
    
    elif  choise == 4 :
        return calc.divide()
    else:
        print("invalid input")

if __name__ == "__main__":
    num1 = int(input("enter the first number:- "))
    num2 = int(input("enter the second number:- "))
    print("*************************************")
    choise = int(input("""
    1 = add
    2 = extraction
    3 = multiplication
    4 = divsion
    """))
    print("*************************************")
    print(ask(num1, num2 , choise))