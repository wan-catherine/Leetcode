"""
pair[0] - pair[1] to get how much we can save if we go to B instead A.
then sort this , let the first N pairs go to A, the last N pairs go to B.
"""
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        N = len(costs) // 2
        costs.sort(key = lambda pair : pair[0]-pair[1])
        res = 0
        for pair in costs:
            if N:
                res += pair[0]
                N -= 1
            else:
                res += pair[1]
        return res
