class UndergroundSystem(object):

    def __init__(self):
        self.average_mapping = {}
        self.id_mapping = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.id_mapping[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        station, checkin = self.id_mapping.pop(id)
        timing = t - checkin
        if (station, stationName) not in self.average_mapping:
            self.average_mapping[(station, stationName)] = [timing, 1]
        else:
            self.average_mapping[(station, stationName)][0] += timing
            self.average_mapping[(station, stationName)][1] += 1

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        if (startStation, endStation) not in self.average_mapping:
            return 0
        timing, ids = self.average_mapping[(startStation, endStation)]
        return timing / ids

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)