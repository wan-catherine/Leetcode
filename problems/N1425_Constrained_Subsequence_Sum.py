import collections
"""
DP
dp[i+1] = nums[i+1] + max(0, dp[i+1-k], dp[i-k], ... , dp[i])

dp[i] means include nums[i+1], the largest sum of the subsequence.

We need to find a O(1) way to find the max(0, dp[i+1-k], dp[i-k], ... , dp[i])
So monotonic stack!!!
"""

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        dp = [nums[0]] * length
        maximum = collections.deque([0])
        for i in range(1, length):
            while maximum and maximum[0] < i - k:
                maximum.popleft()
            dp[i] = nums[i] + max(dp[maximum[0]], 0)
            while maximum and dp[maximum[-1]] < dp[i]:
                maximum.pop()
            maximum.append(i)
        return max(dp)


