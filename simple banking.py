#this is simple program for bank account , it just simple not good for multiple user and store data
#19/08/24 date i know littale bit of function but i can use it becuse i dont know whole thing how to use in this context
count = 0 #password attemp how many try they did
print("welcome to Y2c bank internet banking (for exit type '0' in holder)")
print("--------------------------------------------------------")
        
while True:
    
    holder = input("enter your name:-")
    
    if holder == "0":
        print("thank you!")
        break
    
    passs = input("enter password:- ")
    
    if holder == "bhagyesh" and passs == "bhag12": # check it is existing user or not
        
        print("--------------------------------------")
        print("--------------------------------------")

        print("*******welcome bhagyesh*******")

        print("--------------------------------------")
        print("--------------------------------------")
        
        bhag_bal = 450000
        
        while True:
            print("deposit = press '1' ") #for deposit you have to press 1
            print("credit = press '2' ") #for creadit you have press 2
            print("balence = press '3' ") #for balence check you have to press 
            print("exit = press '0' ")
            
            bhag_input = input("-->" ) #input for transection
            
            if bhag_input == "1":
                print("pls enter your amount you want to deposit")
                bhag_input_dep = int(input("-->"))
                
                if bhag_input_dep < 0: #bhag_input_dep means deposit
                    print("wrong input pls try again!!")

                    print("--------------------------------------")
                    print("--------------------------------------")

                    continue
                bhag_bal = bhag_bal + bhag_input_dep #amount added opration

                print("your transection complet!!")

                print("--------------------------------------")
                print("--------------------------------------")
                
            elif bhag_input == "2":

                print("pls enter your amount you want to credit")
                bhag_input_cre = int(input("-->")) #bhag_input_cre for credit 
                
                if bhag_bal < bhag_input_cre: #check if balnce is lower then total balence or not
                    print("insufficient balance!!")

                    print("--------------------------------------")
                    print("--------------------------------------")
                    continue
                
                bhag_bal = bhag_bal - bhag_input_cre #opration for credit
                    
                print("your transection complet!!")

                print("--------------------------------------")
                print("--------------------------------------")
                
            elif bhag_input == "3":
                
                print(f"your balence is :- {bhag_bal}")

                print("--------------------------------------")
                print("--------------------------------------")
                
            elif bhag_input == "0": #for exiting transection 

                 print("thank you!")

                 print("--------------------------------------")
                 print("--------------------------------------")
                 break
    else:
        print("check your username or password !!!!")
        count += 1 #count password or username attemp if it 3 then exit 
        if count == 3:
            print("you forget your username or password , pls contect your nearest branch")
            print("thank you!")
            break

