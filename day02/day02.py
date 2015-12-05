class Present:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h
        
    def area(self):
        a1 = self.l * self.w
        a2 = self.w * self.h
        a3 = self.h * self.l
        
        extra = min(a1, a2, a3)
        
        return 2 * a1 + 2 * a2 + 2 * a3 + extra
    
    def ribbon(self):
        wrap = (self.l + self.w +  self.h - max(self.l, self.w, self.h)) * 2
        bow = self.l * self.w * self.h
        return wrap + bow

# p1 = Present(2, 3, 4)
# print(p1.area())
# print(p1.ribbon())
#  
# p2 = Present(1, 1, 10)
# print(p2.area())
# print(p2.ribbon())

sumPaper = 0
sumRibbon = 0
with open('input.txt') as f:
    for present in f.readlines():
        present = present.strip()
        splits = present.split('x')
        l = int(splits[0])
        w = int(splits[1])
        h = int(splits[2])
        p = Present(l, w, h)
        sumPaper += p.area()
        sumRibbon += p.ribbon()

print("Paper: " + str(sumPaper))
print("Ribbon: " + str(sumRibbon))
