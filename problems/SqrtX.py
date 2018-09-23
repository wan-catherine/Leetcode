import math
class Solution:
    def mySqrt_slow(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1
        while i * i <= x:
            i += 1
        return i - 1

    def mySqrt(self, x):
        return int(math.sqrt(x))