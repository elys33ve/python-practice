import random

#global
user = 1

#lists for user input (allows a few different inputs to work)
yes = ['yes', 'y']
no = ['no', 'n']
stop = ['exit', 'quit', 'stop']

rock = ['r','rock', 1]
paper = ['p','paper', 2]
scissors = ['s','scissors', 3]

#print at start of game
print("type 'rock', 'paper', or 'scissors' to play")
print("type 'exit' or 'quit' at any point, to leave")

#define game function
def game ():
    global user
    while user not in stop:
        unum = 0
        user = input("")
        num = random.randint(1,3)
        if num == 1:
            num1 = "rock"
        elif num == 2:
            num1 = "paper"
        elif num == 3:
            num1 = "scissors"
        else:
            pass
        if user in rock:
            user = "rock"
            unum = 1
        elif user in paper:
            user = "paper"
            unum = 2
        elif user in scissors:                            #there's probably an easier way to do this
            user = "scissors"                             #i just don't know what it is rn
            unum = 3
        else:
            unum = 10
            print("idk wtf that means pls type 'rock', 'paper', or 'scissors'.")
        if unum == 10:                                    #user input not accepted
            pass
        elif num1 == user:                                #user = computer
            print(num1)
            print("its a tie")
        elif num > unum and num + unum != 4:              #comp = paper, user = rock
            print(num1)                                   #comp = scissors, user = paper
            print("u loose")
        elif unum > num and not(unum + num == 4):         #user = paper, comp = rock
            print(num1)                                   #user = scissors, comp = paper
            print("u win i think")
        elif unum == 1 and num == 3:                      #computer = scissors, user = rock
            print(num1)
            print("u win")
        elif num == 1 and unum == 3:                      #computer = rock, user = scissors
            print(num1)
            print("u loose i think")
        else:                                             #there shouldn't be a way to get this
            print("how tf u get this")                    #(i could use 'pass' or smthn ig, but this is more fun)
    else:
        print("ok bye")                                   #while loop breaks = user chose quit
        exit()
        
#calling the game function (after its defined ^)
game()
