from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        lb, lp = len(buses), len(passengers)
        j = 0
        for i in range(lb):
            cap = capacity
            while j < lp and passengers[j] <= buses[i] and cap > 0:
                if j == 0 or (j >= 1 and passengers[j] - 1 != passengers[j - 1]):
                    res = passengers[j] - 1
                cap -= 1
                j += 1

            if cap > 0:
                if j == 0 or (j >= 1 and passengers[j - 1] != buses[i]):
                    res = buses[i]
        return res
