import random

won = False
played = False

print("You have to guess the number that the computer is thinking of ig")
ht = int(input("how many guesses do u think u will need?\n"))
yes = ['yes', 'y', 'Yes', 'yea']
no = ['n', 'no', 'No', 'nah']


def play ():
    global played
    global i
    global won
    re = 1
    de = 1
    if played == True:
        re = input("would u like to pick a new range?  ")
    else:
        de = input("would u like to pick a range? (otherwise it will be one to ten)\n")
    if re in yes or de in yes:
        ran1 = int(input("what is the lowest number in range?  "))
        ran2 = int(input("cool. what should the highest number be?  "))
    elif de in no:
        ran1 = 1
        ran2 = 10
    elif re in no:
        pass
    else:
        print("huh? u lost ur change range privilages. its 1 to ten")
        ran1 = 1
        ran2 = 10
    won = False
    for i in range(ht):
        cpu = random.randint(ran1,ran2)
        user = int(input("Guess a number between {0} and {1}:  ".format(ran1,ran2)))
        t = ht-(i+1)
        if user == cpu:
            print ("yay u got it. it was {0}".format(user))
            won = True
            playag(i)
        elif user > ran2 or user < ran1:
            print("wtf thats not within the range u fucking idiot")
        else:
            print("no ur fucking wrong. it was {0}".format(cpu))
            print("u have", t, "tries left")
    else:
        playag(i)

def playag (i):
    global played
    played = True
    i = i+1
    if won == True and i == 1:
        pa = input("congrats u got it in {0} time. play again?  ".format(i))
    elif won == True and i != 1:
        pa = input("congrats u got it in {0} times. play again?  ".format(i))
    else:
        pa = input("ur fuckin dumb. it took u {0} tries and u still failed lmao. play again?  ".format(ht))
    if pa in yes:
        play ()
    elif pa in no:
        exit()
    else:
        fucku = input("wtf. idk what that means. type yes or no.")
        if fucku == "no":
            print("k bye")
            exit()
        elif fucku == "yes":
            print("alright whatever")
            play()
        else:
            print("fuck u too i quit")
            exit()

play()
