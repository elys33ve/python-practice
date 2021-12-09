import random

r = 6
pd = False

print("dice roll simulator fuck yeah.\nu can type 'exit' or 'quit' whenever to stop.")
stop = ['quit', 'exit', 'stop']
dice = [4,6,8,10,12,20]

def change ():
    global r
    if pd == True:
        udice = input("what die do u wanna change to (4,6,8,10,12,or 20)?  ")
    else:
        udice = input("do u want a 4, 6, 8, 10, 12, or 20 sided die?  ")
    if udice in stop:
        print("ok bye then already. :|")
        exit()
    elif int(udice) in dice:
        r = int(udice)
        print("good choice ig")
        roll()
    else:
        print("huh? ok lemme repeat.")
        change()
        
    
def roll ():
    global pd
    print("you can change ur die anytime by typing 'dice'.\npress 'enter' to roll.  ")
    user = input(" ")
    while user not in stop and user != 'dice':
        d = random.randint(1,r)
        print(d)
        user = input("  ")
    else:
        if user in stop:
            print("ok bye")
            byebye()
        elif user == 'dice':
            pd = True
            change()
        else:
            print("hmmm idk how u could have gotten this output")
            

def byebye ():
    exit()

change()
