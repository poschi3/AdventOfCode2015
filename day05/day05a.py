import re

p1 = re.compile('.*[aeiou].*[aeiou].*[aeiou].*')
p2 = re.compile('.*(.)\\1{1}.*')
p3 = re.compile('.*(ab|cd|pq|xy).*')

n = 0

with open('input.txt') as f:
    for word in f.readlines():
        #print(word)
        word = word.strip()
        if p1.match(word) is not None:
            #print(1)
            if p2.match(word) is not None:
                #print(2)
                if p3.match(word) is None:
                    #print(3)
                    #print(word)
                    n+=1

print("Words: " + str(n))