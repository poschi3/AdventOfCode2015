
x = 0
y = 0

santamap = dict()

santamap["0:0"] = 1

with open('input.txt') as f:
    for move in f.read():
        if move == '<':
            x-=1
        elif move == '>':
            x+=1
        elif move == 'v':
            y-=1
        elif move == '^':
            y+=1
        
        pos = str(x) + ":" + str(y)

        if pos in santamap:
            santamap[pos] += 1
        else:
            santamap[pos] = 1
            

print("Haushalte: " + str(len(santamap)))