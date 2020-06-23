"""
Key point:
when the ith ligth is on, if there are already i lights on, then it means all i lights on .
"""
class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        count = 0
        right = 0
        res = 0
        for i in light:
            count += 1
            right = max(right, i)
            if count == right:
                res += 1

        return res