import sys
from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        length = len(restrictions)
        if length == 1:
            return n - 1
        limits = [sys.maxsize] * length
        limits[0] = 0
        for i in range(1, length):
            limits[i] = min(limits[i-1] + restrictions[i][0] - restrictions[i-1][0], restrictions[i][1])
        for i in range(length-2, 0, -1):
            limits[i] = min(limits[i], limits[i+1] + restrictions[i+1][0] - restrictions[i][0])

        res = 0
        for i in range(1, length):
            x = (limits[i] - limits[i-1] + restrictions[i][0] - restrictions[i-1][0]) // 2
            res = max(res, x + limits[i-1])
        res = max(res, min(n-1, limits[-1] + n - restrictions[-1][0]))
        return res