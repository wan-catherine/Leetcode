import heapq
from typing import List


class Solution:
    def minRefuelStops_pq(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stack = []
        stations = stations + [[target, 0]]
        length = len(stations)
        left = startFuel
        count = 0
        for i in range(length):
            while stack and left < stations[i][0]:
                left -= heapq.heappop(stack)
                count += 1
            if left < stations[i][0]:
                return -1
            heapq.heappush(stack, -stations[i][1])
        return count

    """
    dp[i] : add i times fuel can travel the longest distance
    """
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations = [[0, startFuel]] + stations
        length = len(stations)
        dp = [0] * length
        dp[0] = startFuel
        for i in range(1, length):
            for j in range(i, -1, -1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
        print(dp)
        for i in range(length):
            if dp[i] >= target:
                return i
        return -1

