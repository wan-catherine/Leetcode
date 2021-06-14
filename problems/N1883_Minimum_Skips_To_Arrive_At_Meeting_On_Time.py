import math
import sys
from typing import List

"""
dp[i][j] : minimum time to spend to travel ith roads and skip j of them. 
for i != the last road, two situations:
    1. don't skip : dp[i][j] = math.ceil dp[i-1][j] + dist[i] / speed - minimum)
    2. skip : dp[i][j] = dp[i-1][j-1] + dist[i] / speed
for i = the last road, there is no need to skip :
    dp[i][j] = dp[i-1][j] + dist[i] / speed
    
Need to minus 1e-10 to avoid the math.ceil to get the wrong answer.

"""

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        dist = [0] + dist
        length = len(dist)
        dp = [[sys.maxsize] * length for _ in range(length)]
        minimum = 1e-10
        dp[0][0] = 0
        for i in range(1, length):
            dp[i][0] = math.ceil(dp[i-1][0] + dist[i] / speed - minimum)
        for i in range(1, length):
            for j in range(1, i+1):
                if i < length - 1:
                    dp[i][j] = min(math.ceil(dp[i-1][j] + dist[i] / speed - minimum), dp[i-1][j-1] + dist[i] / speed)
                else:
                    dp[i][j] = dp[i-1][j] + dist[i] / speed
        for i in range(length):
            if dp[-1][i] <= hoursBefore:
                return i
        return -1