import re

reNumbers = re.compile(r'-?\d+')

f = open('input.txt', 'r')

values = f.read()

sum = 0
for v in reNumbers.findall(values):
    sum += int(v)
print("Total: " + str(sum))