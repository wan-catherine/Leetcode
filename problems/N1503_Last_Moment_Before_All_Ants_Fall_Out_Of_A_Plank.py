"""
Key point is to understand : The ants change their way when they meet is equivalent to continue moving without changing their direction.

We can see ant a and b , when they change their direction after meet at some point,
at this time , we can think a<->b, treat a as b , treat b as a , then the result will be equivalent to continue moving without changing their direction.
We only care time when the last ant fall out of the plank, don't care which ant!!!
"""
class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        res = 0
        for i in left:
            res = max(res, i)
        for i in right:
            res = max(res, n - i)
        return res