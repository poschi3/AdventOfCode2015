import re
reIOL = re.compile(r'[iol]')

def increase(password):
    new = ""
    done = False

    for c in password[::-1]:
        if done:
            new += c
        else:
            if c == "z":
                new += "a"
            else:
                new += chr(ord(c)+1)
                done = True
    return new[::-1]

def isIncreasing(password):
    last = 0
    count = 0
    for c in password:
        act = ord(c)

        if count == 0:
            count = 1
        elif last+1 == act:
            count += 1
        else:
            count = 1
        last = act

        if count >= 3:
            return True
    return False

def isBadLetters(password):
    match = reIOL.search(password)
    return match is None

def isEnoughDouble(password):
    last = ""
    count = 0

    for c in password:
        if c == last:
            count += 1
            last = ""
        else:
            last = c
    return count >= 2

def getNext(pw):

    do = True
    while do:
        pw = increase(pw)
        one = isIncreasing(pw)
        two = isBadLetters(pw)
        three = isEnoughDouble(pw)

        do = one and two and three
        do = not do

    return(pw)

pw = "hxbxwxba"
one = getNext(pw)
print("Teil 1: " + one)
two = getNext(one)
print("Teil 2: " + two)