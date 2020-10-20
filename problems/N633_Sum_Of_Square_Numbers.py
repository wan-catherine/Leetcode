import math


class Solution(object):
    def judgeSquareSum_slow(self, c):
        """
        :type c: int
        :rtype: bool
        """
        k = int(math.sqrt(c))
        for i in range(k+1):
            b = math.sqrt(c - i*i)
            if b == int(b):
                return True
        return False

    def judgeSquareSum(self, c):
        l,r = 0, int(math.sqrt(c))
        while l <= r:
            cur = l*l + r*r
            if cur < c:
                l += 1
            elif cur > c:
                r -= 1
            else:
                return True
        return False