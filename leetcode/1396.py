class UndergroundSystem:

    def __init__(self):
        self.departures = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.departures[id] = (stationName, t)

    def checkOut(self, id: int, arr: str, t: int) -> None:
        (dep, start) = self.departures[id]
        del self.departures[id]
        if dep not in self.times:
            self.times[dep] = {}
        if arr not in self.times[dep]:
            self.times[dep][arr] = []
        self.times[dep][arr].append(t - start)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.times[startStation][endStation])/len(self.times[startStation][endStation])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)