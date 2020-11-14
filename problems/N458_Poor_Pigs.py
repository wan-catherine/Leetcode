"""
Notice, a pig can drink more than one bucket at the same time.
For each one pig, we can have val = (minutesToTest // minutesToDie + 1) status .
So for n pigs, we can have val ** n status. 
"""
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        val = minutesToTest // minutesToDie + 1
        res = 0
        while val ** res < buckets:
            res += 1
        return res