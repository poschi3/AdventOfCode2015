routes = dict()
citys = set()

def add_route(a, b, cost):
    if not a in routes:
        routes[a] = dict()
    routes[a][b] = int(cost)

def get_costs(start, currentcosts, opendesinations):
    if len(opendesinations) <= 0:
        return 0, 0
    minimum = 999999999999
    maximum = 0
    for city in opendesinations:
        todo = set(opendesinations)
        todo.remove(city)
        minCosts, maxCosts = get_costs(city, currentcosts, todo)
        if start != '':
            minCosts += routes[start][city]
            maxCosts += routes[start][city]
        minimum = min(minimum, minCosts)
        maximum = max(maximum, maxCosts)
    return currentcosts + minimum, currentcosts + maximum

with open('input.txt') as f:
    for q in f.readlines():
        split = q.strip().split()
        
        a = split[0]
        b = split[2]
        cost = split[4]
        
        add_route(a, b, cost)
        add_route(b, a, cost)
        
        citys.add(a)
        citys.add(b)
        
    minimum, maximum = get_costs('', 0, citys)
    print("Minimum distance is " + str(minimum))
    print("Maximum distance is " + str(maximum))
