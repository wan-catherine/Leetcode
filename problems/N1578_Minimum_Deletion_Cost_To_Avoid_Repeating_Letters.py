class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        length = len(s)
        for i in range(length - 1):
            if s[i] != s[i+1]:
                if stack:
                    res += sum(cost[stack[0]:i+1]) - max(cost[stack[0]:i+1])
                    stack = []
                continue
            stack.append(i)
            if i == length - 2:
                res += sum(cost[stack[0]:]) - max(cost[stack[0]:])
        return res
