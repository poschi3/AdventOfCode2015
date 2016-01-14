import re

def tableSum(order):
    sum = 0
    last = None
    for act in order:
        if last == None:
            sum += persons[order[-1]][act]
            sum += persons[act][order[-1]]
        else:
            sum += persons[last][act]
            sum += persons[act][last]
        last = act
    return sum

reg = re.compile(r'^(\w+).*(gain|lose).* (\d+).* (\w+)\.$')

persons = dict()

with open('input.txt') as f:
    for line in f.readlines():
        match = reg.match(line)
        person = match.group(1)
        plusminus = match.group(2)
        value = int(match.group(3))
        by = match.group(4)

        if plusminus == "lose":
            value *= -1

        if not person in persons:
            persons[person] = dict()

        persons[person][by] = value

names = list()
for name in persons:
    names.append(name)

def tryOrders(act, rest):
    if len(rest) == 0:
        return tableSum(act)
    else:
        maxVal = 0
        for r in rest:
            new_act = act[:]
            new_act.append(r)
            new_rest = rest[:]
            new_rest.remove(r)
            s = tryOrders(new_act, new_rest)
            maxVal = max(maxVal, s)
        return maxVal

print("Ohne mich " + str(tryOrders(list(), names)))

me = "Me"

persons[me] = dict()

for name in names:
    persons[name][me] = 0
    persons[me][name] = 0
names.append(me)

print("Mit mir " + str(tryOrders(list(), names)))