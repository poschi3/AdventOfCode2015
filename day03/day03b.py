class Pos:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def changePos(self, move):
        if move == '<':
            self.x-=1
        elif move == '>':
            self.x+=1
        elif move == 'v':
            self.y-=1
        elif move == '^':
            self.y+=1
        else:
            print("Error")
        
    def getPos(self):
        return str(self.x) + ":" + str(self.y)
        

santa = Pos()
robo = Pos()

santamap = dict()

santamap["0:0"] = 2

person = True

with open('input.txt') as f:
    for move in f.read():
        
        if person:
            santa.changePos(move)
            pos = santa.getPos()
        else:
            robo.changePos(move)
            pos = robo.getPos()

        if pos in santamap:
            santamap[pos] += 1
        else:
            santamap[pos] = 1
            
        person = not person
            

print("Haushalte: " + str(len(santamap)))

