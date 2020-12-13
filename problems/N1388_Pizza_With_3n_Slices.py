"""
Similar with House Robber problem.

In order to solve the circular issue, we can loop twice, one is with first, another is with last.
dp[i][j] : from the first ith elements , pick j element to get the maximum sum of those j elements.
"""
class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        def helper(arr):
            length = len(arr)
            unit = (length+1) // 3
            dp = [[0]*(unit+1) for _ in range(length+1)]
            for i in range(1, length+1):
                for j in range(1, unit+1):
                    dp[i][j] = max(dp[i-1][j], arr[i-1] + (dp[i-2][j-1] if i >= 2 else 0))
            return dp[-1][-1]

        return max(helper(slices[1:]), helper(slices[:-1]))
