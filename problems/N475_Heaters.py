import bisect
from typing import List


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        length = len(heaters)
        res = 0
        for h in houses:
            index = bisect.bisect(heaters, h)
            if index == 0:
                dist = heaters[0] - h
            elif index == length:
                dist = h - heaters[length-1]
            else:
                dist = min(h-heaters[index-1], heaters[index]-h)
            res = max(res, dist)
        return res

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        lh, lt = len(houses), len(heaters)
        houses.sort()
        heaters.sort()

        def check(m):
            covered = [0] * lh
            i, j = 0, 0
            while i < lh and j < lt:
                if covered[i]:
                    i += 1
                    continue
                if abs(heaters[j] - houses[i]) <= m:
                    covered[i] = 1
                    i += 1
                else:
                    j += 1
            return sum(covered) == lh

        l, r = 0, 10 ** 9
        while l < r:
            mid = (r - l) // 2 + l
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

