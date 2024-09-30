import random
number = random.randint(1,100)
count = 0
while True:
    user_number = int(input("enter the number :- "))
    if user_number == number :
        if count == 1:
            print("congatulation you guess the number in just 1 guess!! ")
            break
        else:
            print(f"ohh you guess the number in {count}")
            break
    elif user_number> number:
        print("its high")
        count += 1
    elif user_number< number:
        print("its low")
        count +=1