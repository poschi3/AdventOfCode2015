import re

leftright = re.compile("^(.*)\s->\s(.*)$")

instructions = dict()
results = dict()

def get_value(var):
    if var.isdigit():
        return int(var)
    
    if var in results:
        return results[var]
        
    value = evaluate(var)
    results[var] = value
    return int(value)

def evaluate_three(split):
    left, op, right = split
    
    if op == 'AND':
        return get_value(left) & get_value(right)
    elif op == 'OR':
        return get_value(left) | get_value(right)
    elif op == 'LSHIFT':
        return get_value(left) << get_value(right)
    elif op == 'RSHIFT':
        return get_value(left) >> get_value(right)
    else:
        raise ValueError('Operation ' + op + ' is unknown')
    
def evaluate_two(split):
    return ~ get_value(split[1])

def evaluate_one(split):
    return get_value(split[0])

def evaluate(var):
    left = instructions[var]
    split = left.split()
    
    if len(split) == 3:
        return evaluate_three(split)
    elif len(split) == 2:
        return evaluate_two(split)
    elif len(split) == 1:
        return evaluate_one(split)
    else:
        raise ValueError('Operation ' + left + ' has to many parts')
    
# Befehle einlesen:    
with open('input.txt') as f:
    for line in f.readlines():
        instruction = line.strip()
        
        m = leftright.match(instruction)
        left = m.group(1)
        right = m.group(2)
        
        instructions[right] = left

a = get_value("a")
        
print("A entspricht " + str(a))

results = dict()
results["b"] = a 

print("A' entspricht " + str(get_value("a")))
