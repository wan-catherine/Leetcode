import sys
"""
Two key points : 
    1. Manhattan distance : smallest sum of Manhattan distance to all points is the median point 
    2. interval dp (split into k groups)
"""

class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        length = len(houses)
        if k == length:
            return 0
        houses.sort()
        manhattandis = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(i, length):
                median = (i + j) // 2
                for p in range(i, j + 1):
                    manhattandis[i][j] += abs(houses[p] - houses[median])
        print(manhattandis)
        # hourse = [0] + houses
        dp = [[sys.maxsize] * (k + 1) for _ in range(length + 1)]

        for i in range(1, length + 1):
            dp[i][1] = manhattandis[0][i - 1]

        for i in range(1, length + 1):
            for j in range(2, k + 1):
                for p in range(1, i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + manhattandis[p][i - 1])
        print(dp)
        return dp[-1][-1]