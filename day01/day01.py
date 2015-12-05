f = open('input.txt', 'r')

values = f.read()

floor = 0
i = 0
foundBasement = False

for a in values:
    i+=1
    if a == "(":
        floor+=1
    else:
        floor-=1
        
    if floor == -1 and not foundBasement:
        foundBasement = True
        print("Basement found at position " + str(i))
        
print("Last floor : " + str(floor))
