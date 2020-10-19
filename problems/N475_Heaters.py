import bisect


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

