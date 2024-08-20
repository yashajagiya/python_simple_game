import random #import random so computer choice randomly

sps = ["Rock", "Paper", "Scissors"] #list for choice randomly

print("lets play 'Rock Paper Scissors'")
print(" its best of 5")
print("'1'--> Rock") #for Rock user press 1
print("'2'--> Paper") #for Paper user press 2
print("'3'--> Scissors") #for Scissors user press 3
print("for End and show score press '0'..")

score = 0 #use score
com_score = 0 # compuer score
draw = 0 #for count the tie round 
rounds = 0 #round counf

while True:

    user = input("pleas choice betwen '1. Rock' '2. paper' '3. scissors' :- ") #input is string
    com_choice = random.choice(sps) #computer choice randomly

    if user != "1" and user != "2" and user != "3" and user != "0": #condision for check if use input is out of 1 2 3 if not then rewrite input
        print("wrong input pls choice between '1' , '2' , '3' ")
        continue

    if (user == "1" and com_choice == "Rock") or (user == "2" and com_choice == "Paper") or (user == "3" and com_choice == "Scissors"):
        #for chek it user and computer choice  is same

        if user == "1":
            print(f"you choce 'Rock' and computer choice '{com_choice}'") #show the what use choice and computer choice
        elif user == "2":
            print(f"you choce 'Paper' and computer choice '{com_choice}'") #show the what use choice and computer choice
        elif user == "3":
            print(f"you choce 'Scissors' and computer choice '{com_choice}'") #show the what use choice and computer choice
        print("ohh its draw!!")
        draw += 1 #if its draw then count incress
        rounds += 1 #it count rounds
        print("---------------------------------------------------------------------------------------------------")

    elif ( user == "1" and com_choice == "Scissors") or ( user == "2" and com_choice == "Rock") or ( user == "3" and com_choice == "Paper"):

        if user == "1":
            print(f"you choce 'Rock' and computer choice '{com_choice}'") #show the what use choice and computer choice
        elif user == "2":
            print(f"you choce 'Paper' and computer choice '{com_choice}'") #show the what use choice and computer choice
        elif user == "3":
            print(f"you choce 'Scissors' and computer choice '{com_choice}'") #show the what use choice and computer choice

        print("congratulations!! you win")
        print("---------------------------------------------------------------------------------------------------")

        score += 1 #if user win the its socore incress
        rounds += 1 #it count rounds


    elif (user == "3" and com_choice == "Rock") or (user == "2" and com_choice == "Scissors") or (user == "1" and com_choice == "Paper"):
        #condiston when user loss 

        if user == "1": 
            print(f"you choce 'Rock' and computer choice '{com_choice}'") #show the what use choice and computer choice
        elif user == "2":
            print(f"you choce 'Paper' and computer choice '{com_choice}'") #show the what use choice and computer choice
        elif user == "3":
            print(f"you choce 'Scissors' and computer choice '{com_choice}'") #show the what use choice and computer choice

        print("computer win!!")
        print("---------------------------------------------------------------------------------------------------")

        com_score += 1 #if computer win then its score incerss
        rounds += 1#it count rounds


    if user == "0" or rounds == 5: #if user want to exits by press 0 or round count is 5

        if com_score > score: #if computer score is more then user
            print(f"computer socor = {com_score} , your score is {score} , draw rounds {draw}")
            print("computer win this game, better luck next time")

        elif score> com_score: #if user score is more then computer
            print(f"your score is {score} , computer socor = {com_score}  , draw rounds {draw}")
            print("congratulations!! you win The Game")

        elif score == com_choice: #if user and compuetr have same score
            print(f"your score is {score} , computer socor = {com_score}  , draw rounds {draw}")
            print("congratulations!! you and computer have same score")
        
    
        print("thank you for playing!!")
        break
