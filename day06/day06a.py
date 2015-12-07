import re

p = re.compile("^(\D+)\s(\d+),(\d+)\s\D+\s(\d+),(\d+)$")

lights = [[False for x in range(1000)] for x in range(1000)]

with open('input.txt') as f:
    for inst in f.readlines():
        m = p.match(inst)
        action = m.group(1)

        x1 = int(m.group(2))
        y1 = int(m.group(3))
        x2 = int(m.group(4))
        y2 = int(m.group(5))
                
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == 'turn on':
                    lights[x][y] = True
                elif action == 'turn off':
                    lights[x][y] = False
                elif action == 'toggle':
                    lights[x][y] = not lights[x][y]
                   
on = 0
off = 0

for x in lights:
    for y in x:
        if y:
            on+=1
        else:
            off+=1
            
print("On " + str(on) + "; Off " + str(off))
