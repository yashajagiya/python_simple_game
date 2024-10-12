num = int(input("enter number:- "))
if num > 1:
    print("* "*num)
    num2 = num - 2
    for i in range(num2):
        print("* "+" "*(num2*2)+"*")
    print("* "*num)
else:
    print("1 squre is not possible")