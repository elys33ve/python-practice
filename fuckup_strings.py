#mess with strings
    #1: abcd --> aababcabcd
    #2: abcd --> dcba
    #3: abcd --> aaabbbcccddd


def fuckup_string ():
    print("input a string (preferably a one word, short one but whatever)")
    string = input("string:  ")
    slen = len(string[:])
    #set variables outside loop
    s1 = ''
    s3l = []
    for i in range(slen):       #string 1
        x = i + 1
        s1 = s1 + str(string[:x])
    s2 = string[::-1]           #string 2
    for i in range(slen):       #string 3
        for ii in range(3):
            s3l.append(string[i])
    s3 = ''.join(s3l)
    print(s1)
    print(s2)
    print(s3)
        

fuckup_string()
