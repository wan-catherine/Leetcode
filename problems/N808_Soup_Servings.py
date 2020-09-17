"""
When we need to calculate the probability of some events (here is A empty than B or A and B empty together).
We can convert it into different operations .
We have 4 operations here , and each operation has 0.25 probaility.
"""
class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        # the all four operation, can server A 250, B 150. It means the larger N is , the larger possibility A wll be empty first.
        if N > 5000:
            return 1
        memo = {}
        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a > 0 and b <= 0:
                return 0
            if a <= 0 and b > 0:
                return 1
            if a <= 0 and b <= 0:
                return 0.5

            memo[(a, b)] = 0.25*(dfs(a-100, b) + dfs(a-75, b-25) + dfs(a-50, b-50) + dfs(a-25, b-75))
            return memo[(a, b)]
        return dfs(N, N)

