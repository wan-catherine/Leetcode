class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        res = abs(6 * minutes - (minutes / 2 + hour * 30))
        if res > 180:
            res = 360 - res

        return res
