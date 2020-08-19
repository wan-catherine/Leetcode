class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if not timePoints:
            return
        times = []
        for point in timePoints:
            times.append(int(point[:2])*60 + int(point[3:]))
        times.sort()
        res = 24*60
        length = len(times)
        for i in range(1, length):
            res = min(res, times[i] - times[i-1])
        res = min(res, times[0] + 24*60 - times[-1])
        return res