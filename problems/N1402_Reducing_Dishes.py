"""
This is a great tricky problem.
"""
class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse=True)
        res, total = 0, 0
        for s in satisfaction:
            total += s
            if total > 0:
                res += total
        return res