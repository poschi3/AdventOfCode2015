import Queue

def count_string(line):
    chars = 0
    q = Queue.Queue()
    for c1 in line:
        q.put(c1)
    
    while not q.empty():
        c1 = q.get()
        if c1 == '\\':
            c2 = q.get()
            
    # \\ (which represents a single backslash)
            if c2 == '\\':
                chars += 1
    # \" (which represents a lone double-quote character)
            elif c2 == '\"':
                chars += 1
    # \x plus two hexadecimal characters (which represents a single character with that ASCII code).
            elif c2 == 'x':
                q.get()
                q.get()
                chars += 1
            else:
                raise ValueError("Parsing Error " + line + " at char " + c1 + c2)

        elif c1 == "\"":
            pass
        
        else:
            chars += 1
            
    return len(line) - chars 
            

def encode_string(line):
    out = '"'
    
    for c in line:
        if c == '"':
            out += '\\"'
        elif c == '\\':
            out += '\\\\'
        else:
            out += c
    out += '"'
    return out
    
totalA = 0
totalB = 0

with open('input.txt') as f:
    for q in f.readlines():
        q = q.strip()
        
        totalA += count_string(q)
        totalB += len(encode_string(q)) - len(q)
        
print("Sum A " + str(totalA))
print("Sum B " + str(totalB))
