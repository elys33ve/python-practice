#recursion/fibonacci numbers

x = int(input("x =  "))             #user input for x

def recursion (x):                  #define the function that recurs
    if x > 0:
        y = x + recursion(x-1)      #recursion happens in + recursion(x-1)
        print(y)
    else:
        y = 0
    return y

recursion(x)

#### Function will: (if x = 6)
#
# 6 > 0, so y = 6 + rec(5)
# 5 > 0, so y = 5 + rec(4)
# 4 > 0, so y = 4 + rec(3)
# 3 > 0, so y = 3 + rec(2)
# 2 > 0, so y = 2 + rec(1)
# 1 > 0, so y = 1 + rec(0)
# 0 not > 0, so y = 0
# rec(1) = 1 + 0 = 0
# so y = 1, and returns 1
# rec(2) = 2 + 1 = 3
# so y = 3, and returns 3
# rec(3) = 3 + 3 = 6
# so y = 6, and returns 6
# rec(4) = 4 + 6 = 10
# so y = 10, and returns 10
# rec(5) = 5 + 10 = 15
# so y = 15, and returns 15
# rec(6) = 6 + 15 = 21
# so y = 21, and returns 21
#
#output will be:
#
#0
#1
#3
#6
#10
#15
#21

