import re

p = re.compile(r'(.)\1*')

def proceed(input):
    out = ""
    it = p.finditer(input)
    for match in it:
        part = match.group()
        out += str(len(part))
        out += part[0]
    return out

input = "1113222113"
for x in range(0, 40):
    input = proceed(input)
print("Teil 1: " + str(len(input)))

for x in range(0, 10):
    input = proceed(input)
print("Teil 2: " + str(len(input)))
