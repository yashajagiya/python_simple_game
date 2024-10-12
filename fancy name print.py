import time  
def fancy_name(name : str):
    alphabet = [  
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',   
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'  ]  
    fname = ""  
    count = 0  
    while count < len(name):  
        for i in alphabet:  
            print(fname + i,)
            time.sleep(0.1)  
            if name[count] == i:  
                count += 1  
                fname += i
                break

if __name__ == "__main__":
    name = input("Enter Your Name: ").upper()  
    fancy_name(name)