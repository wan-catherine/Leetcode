import math


class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        one = math.sqrt(num+1)
        if int(one) == one:
            return [int(one), int(one)]
        two = math.sqrt(num+2)
        if int(two) == two:
            return [int(two), int(two)]
        val = int(two)

        res = []
        """
        We don't need to compare all of them . 
        if a * b = c * d and a < c< sqrt(x+1) || sqrt(x+2) < d < b, we can have b - a > d - c.
        """
        for i in range(val, 0, -1):
            if not (num+1) % i:
                v = (num+1)//i
                # if not res or abs(i - v) < abs(res[0] - res[1]):
                return [i, v]
            if not (num+2) % i:
                v = (num+2)//i
                # if not res or abs(i - v1) < abs(res[0] - res[1]):
                #     res = [i, v1]
                return [i, v]
        # return res

