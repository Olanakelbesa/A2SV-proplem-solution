class UndergroundSystem:

    def __init__(self):
        self.timeDict = defaultdict(list)
        self.checkInDict = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInDict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        inStation, inTime = self.checkInDict[id]
        del self.checkInDict[id]
        self.timeDict[(inStation, stationName)].append((t - inTime))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        res = 0
        for time in self.timeDict[(startStation, endStation)]:
            res += time
        return res / (len(self.timeDict[(startStation, endStation)]))


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)