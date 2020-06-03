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
