import re

p1 = re.compile('.*(.{2}).*\\1.*')
p2 = re.compile('.*(.).\\1.*')

n = 0

with open('input.txt') as f:
    for word in f.readlines():
        #print(word)
        word = word.strip()
        if p1.match(word) is not None:
            #print(1)
            if p2.match(word) is not None:
                #print(2)
                n+=1

print("Words: " + str(n))