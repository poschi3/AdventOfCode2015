import re

p = re.compile("^(\D+)\s(\d+),(\d+)\s\D+\s(\d+),(\d+)$")

lights = [[0 for x in range(1000)] for x in range(1000)]

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
                    lights[x][y]+= 1
                elif action == 'turn off':
                    lights[x][y] -=1
                    if lights[x][y] < 0:
                        lights[x][y] = 0
                elif action == 'toggle':
                    lights[x][y] += 2
                   
brightness = 0

for x in lights:
    for y in x:
        brightness+= y
            
print("Brightness " + str(brightness))
