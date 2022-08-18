# ahah genshin wishes
# https://www.reddit.com/r/Genshin_Impact/comments/jo9d9d/the_5_rate_is_not_uniform_06_there_is_a_soft_pity/
# https://genshin-wishes.com/global-stats/all
# https://genshin-impact.fandom.com/wiki/Wishes

# i sacrificed a night's sleep for this and it may be one of the sloppiest functional scripts i have
# bc damn i do not want to have to re figure out what that middle stuff does
# (nor do i want to have to verify the accuracy of the statistics and stuff)
# time to just get one of those tracking app things like i should have done to begin with


### file 
event_file = "event_pulls.txt"
promo_file = "promo_pulls.txt"

### constants
EVENT = 'event'
PROMO = 'promo'
WEAPON = 'weapon'       # idc

# character event wishes
GTEE_RATE = 0.994        # (4 star 0.5, 5 star 0.006)

BASE_RATE_S4 = 0.051
GTEE_S4 = 10
GTEE_S4C = 20
SOFT_PITY_S4 = 8

BASE_RATE_S5 = 0.006
GTEE_S5 = 90
GTEE_S5C = 180       # (50% on first guarantee)
SOFT_PITY_S5 = 75
AVG_D_S5 = 75


### globals
pulls = []


### functions
def wish_type (wish):
    if wish == EVENT:
        file = event_file
    elif wish == PROMO:
        file = promo_file

    r, a = open(file, 'r'), open(file, 'a')
    l = r.readlines()

    return l, a, r



def add_pulls (wish=EVENT):
    l, a, r = wish_type(wish)

    stars = ['1', '2', '3', '4', '4c', '5', '5c']       # 'c' = character
    item = '1'
    while item in stars:
        item = input("")
        pulls.append(item)
    
    del pulls[len(pulls)-1]

    cnt = len(l[len(l)-1])          # num chars in last line
    print(cnt)
    for i in range(len(pulls)):
        if cnt >= 30:               # 10 items in line = newline
            a.write("\n")
            cnt = 0
        if pulls[i] == '4c' or pulls[i] == '5c':
            a.write(f"{pulls[i]} ")
        else:
            a.write(f"{pulls[i]}  ")
        cnt += 3
    
    a.close()



### get next pity
def get_pity (wish=EVENT, void=1):
    l, a, r = wish_type(wish)

    w4, w5, c4, c5 = -1, -1, -1, -1     # 4-5 weapon, 4-5 character
    stars = [w4, w5, c4, c5]

    if wish == EVENT:
        w5 = 500

    for i in range(-len(l)+1, 1):
        if -1 not in stars:
            break

        temp = l[i*(-1)].strip().split(' ')
        while '' in temp:
            temp.remove('')
        for j in range(-len(temp)+1, 1):
            pulls.append(temp[j*(-1)])


        if '5c' in pulls:                   # last 5 star char
            c5 = pulls.index('5c')
        if '5' in pulls:                    # last 5 star weapon
            w5 = pulls.index('5')
        if '4c' in pulls:                   # last 4 star char
            c4 = pulls.index('4c')
            if c5 < c4:
                c4 = c5
            if w5 < c4:
                c4 = w5
        if '4' in pulls:                    # last 4 star item
            w4 = pulls.index('4')
            if c5 < w4:
                w4 = c5
            if w5 < w4:
                w4 = w5
            if c4 < w4:
                w4 = c4


    next_gtee_4w = GTEE_S4 - w4
    next_gtee_4c = GTEE_S4C - c4
    if wish == EVENT:
        if w5 != 500 and w5 < c5:
            c5 = w5
        next_gtee_5c = GTEE_S5C - c5 - 90
        next_gtee_5w = next_gtee_5c
    elif wish == PROMO:
        next_gtee_5w = GTEE_S5 - w5
        next_gtee_5c = GTEE_S5C - c5


    if void == 1:
        print()
        print(f"next 4* item guarantee: {next_gtee_4w}")
        print(f"next 4* character guarantee: {next_gtee_4c}")
        if wish == EVENT:
            print(f"next 5* character guarantee: {next_gtee_5c}")
        elif wish == PROMO:
            print(f"next 5* item guarantee: {next_gtee_5w}")
            print(f"next 5* character guarantee: {next_gtee_5c}")
    elif void == 0:
        return next_gtee_4w, next_gtee_4c, next_gtee_5w, next_gtee_5c


### find stats for 4 star item and character
def star4_stats (w4g, c4g):
    c4_gtee = False

    if w4g > 2:                     # 4* item
        w4_stat = BASE_RATE_S4
    elif w4g <= 2 and w4g > 0:
        w4_stat = (((GTEE_RATE - BASE_RATE_S4) / (GTEE_S4-SOFT_PITY_S4 + 1)) * ((GTEE_S4-SOFT_PITY_S4 + 1) - w4g)) + BASE_RATE_S4
    elif w4g <= 0:
        w4_stat = GTEE_RATE
    
    if c4g-10 < w4g:                # 4* character
        c4_stat = w4_stat
        c4_gtee = True
    elif c4g-10 >= w4g:
        if c4g > GTEE_S4-SOFT_PITY_S4:
            c4_stat = BASE_RATE_S4
        elif c4g <= GTEE_S4-SOFT_PITY_S4 and c4g > 0:
            c4_stat = ((((GTEE_RATE - BASE_RATE_S4) / (GTEE_S4-SOFT_PITY_S4 + 1)) * ((GTEE_S4-SOFT_PITY_S4 + 1) - c4g)) + BASE_RATE_S4) / 2
        else:
            c4_stat = GTEE_RATE / 2

    return w4_stat, c4_stat, c4_gtee


### find stats fpr 5 star item and character
def star5_stats (w5g, c5g, wish):
    c5_gtee = False

    if w5g <= 0:                    # 5* item
        w5_stat = GTEE_RATE
    else:
        if w5g > GTEE_S5-SOFT_PITY_S5:
            w5_stat = BASE_RATE_S5
        elif w5g <= 0:
            w5_stat = GTEE_RATE
        else:
            w5_stat = (((GTEE_RATE - BASE_RATE_S5) / (GTEE_S5-SOFT_PITY_S5 + 1)) * ((GTEE_S5-SOFT_PITY_S5 + 1) - w5g)) + BASE_RATE_S5
    
    if wish == EVENT:               # 5* character
        if c5g <= 0:
            c5_stat = GTEE_RATE
        else:
            if c5g > 15:
                c5_stat = BASE_RATE_S5
            elif c5g <= 0:
                c5_stat = GTEE_RATE
            else:
                c5_stat = (((GTEE_RATE - BASE_RATE_S5) / (GTEE_S5-SOFT_PITY_S5 + 1)) * ((GTEE_S5-SOFT_PITY_S5 + 1) - c5g)) + BASE_RATE_S5
    else:
        if c5g-90 < w5g:
            c5_stat = w5_stat
            c5_gtee = True
        elif c5g-90 >= w5g:
            c5_stat = w5_stat

    return w5_stat, c5_stat, c5_gtee

### ahaha this is unorganized
def star5_ten (c5g):
    if c5g <= 0:
            c5_stat = GTEE_RATE
    else:
        if c5g > 15:
            c5_stat = BASE_RATE_S5
        elif c5g <= 0:
            c5_stat = GTEE_RATE
        else:
            c5_stat = (((GTEE_RATE - BASE_RATE_S5) / (GTEE_S5-SOFT_PITY_S5 + 1)) * ((GTEE_S5-SOFT_PITY_S5 + 1) - c5g)) + BASE_RATE_S5
    return c5_stat


### format and print stats
def get_stats (wish=EVENT):
    w4g, c4g, w5g, c5g = get_pity(wish, void=0)

    w4_stat, c4_stat, c4_gtee = star4_stats(w4g, c4g)
    w5_stat, c5_stat, c5_gtee = star5_stats(w5g, c5g, wish)

    for i in range(2):
        print()
        if i == 0:
            print("(on next pull)")
            w4_stat *= 100
            c4_stat *= 100
            w5_stat *= 100
            c5_stat *= 100
            print(f"probability of 4* item: {w4_stat:.2f}%")
            print(f"probability of 4* character: {c4_stat:.3f}%\t\tnext guarantee = {c4_gtee}")
            if wish == EVENT:
                print(f"probability of 5* character: {c5_stat:.3f}%")
            else:
                print(f"probability of 5* item: {w5_stat:.3f}%")
                print(f"probability of 5* character: {c5_stat:.3f}%\t\tnext guarantee = {c5_gtee}")            
        
        else:
            print("(next 10 pulls)")
            c5 = 1 
            if c5g > 25:
                c5 = (1 - BASE_RATE_S5)**10
                #c5 = 0.005983825892803996 * 100 
            else:
                for j in range(10):
                    c5 *= (1 - star5_ten(c5g))
                    c5g += 1
            c5 = 1 - c5
            c5 *= 100
            print(f"4* character guarantee: {c4_gtee}")
            print(f"probability of 5* character: {c5:.3f}%")
        


if __name__ == "__main__":
    #add_pulls()
    get_pity()
    get_stats()
