import random
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '/', '<', '>', '?', '`', '~', ' ']
# list of charcter that be using in string
key = char.copy() #make copy of char so we shuffle it
random.shuffle(key) #shuffle the char list
message = input("enter the secreet message:- ") #input the message that you want to encrypt
encryption_msg = "" #for saving the decrypted msg
for i in message:
    index = char.index(i) #check the where is the message[index] in char list 
    encryption_msg += key[index] 
    #encryption = key(shuffle)[index] means exampl "a" is in char[0] so,
    #we use shuffle key rendomly so we use the char[index] to key[index] means,
    #for eample if message is "a" and in char is a[0] and in key [0] is j means that return j as decryption messge
    #just like that we use multile char as main list that unmuteble and that use for serche the message[index]
print(f"your rncript message {encryption_msg}")

print("------------------------")
print("-------decryption-------")

decryption_msg = input("enter the discript msg :- ")
decryption = ""

for y in decryption_msg:
    index = key.index(y) #now that decryption string index 0 serch in the key list and then 
    #it index number that is serch on the char list and that word shoud be encryption verson of the that string 
    #for example we previseli consider a[0] as messag and j[0] is our decryption so in this lopp we see where is j index
    # acordig to example it on index 0 so we see on the char[0] word that is a so we got the encryption decryption program
    decryption += char[index]
print(f"your decryption message:-{decryption}")