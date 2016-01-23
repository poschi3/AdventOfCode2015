totalflight = 2503
kmmax = 0
winner = None
reindeers = list()


class Reindeer:
    def __init__(self, name, speed, duration, pause):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.pause = pause

        self.points = 0

    def distanceAt(self, flight):
        iteration = self.duration + self.pause

        km = flight // iteration * self.duration * self.speed
        rest = flight % iteration

        km += min(rest, self.duration) * self.speed


        return km

    def __unicode__(self):
        return self.name + " " + str(self.points)

with open('input.txt') as f:
    for line in f.readlines():
        s = line.split(' ')
        r = Reindeer(s[0], int(s[3]), int(s[6]), int(s[13]))
        reindeers.append(r)

        km = r.distanceAt(totalflight)

        if(kmmax <= km):
            winner = r
            kmmax = km

print(winner.name, kmmax, "\n")

for i in range(1, totalflight +1):

    roundpoints = dict()
    maxpoint = 0
    for r in reindeers:
        points = r.distanceAt(i)
        roundpoints[r] = points
        maxpoint = max(maxpoint, points)

    for r, point in roundpoints.items():
        if point == maxpoint:
            r.points += 1

reindeers.sort(key=lambda r: r.points, reverse=True)

print(reindeers[0].name, reindeers[0].points)





