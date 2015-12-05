import hashlib


secret = "yzbqklnj"

counter = -1

searching = True
while searching:
    counter+=1

    m = hashlib.md5()
    m.update(secret + str(counter))
    hash = m.hexdigest()

    searching = (hash[0:5] != "00000")
    #print(counter)

print("Counter " + str(counter) + " Hash " + hash)
    
