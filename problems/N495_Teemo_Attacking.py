class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0

        res = 0
        length = len(timeSeries)
        for i in range(1, length):
            if timeSeries[i] > timeSeries[i-1] + duration -1:
                res += duration
            else:
                res += timeSeries[i] - timeSeries[i-1]
        res += duration
        return res
