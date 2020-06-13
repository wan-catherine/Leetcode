"""
DP
There are two status:
    nums[i] (>=<) nums[i-1]

    ith is decrease/increase

For ith, we have two situation , dp[i][0] means decrease, dp[i][1] means increase

when nums[i] > nums[i-1], it should be increase
dp[i][1] = max(dp[i-1][0] + 1, dp[i-1][1])
    i-1 days is descrease, so add one day, or doesn't include ith day
dp[i][0] = dp[i-1][0] : doesn't include ith day

when nums[i] < nums[i-1], it should be decrease
dp[i][0] = max(dp[i-1][1] + 1, dp[i-1][0])
    i-1 days is increase, so add one day, or doesn't include ith day
dp[i][1] = dp[i-1][1] : doesn't include ith day

when nums[i] == nums[i-1], it should remove ith day:
dp[i][0] = dp[i-1][0]
dp[i][1] = dp[i-1][1]
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_len = len(nums)
        dp = [[1]*2 for _ in range(nums_len)]
        for i in range(1,nums_len):
            if nums[i] - nums[i-1] > 0:
                dp[i][1] = max(dp[i - 1][0] + 1, dp[i - 1][1])
                dp[i][0] = dp[i-1][0]
            elif nums[i] - nums[i-1] < 0:
                dp[i][0] = max(dp[i-1][1] + 1, dp[i-1][0])
                dp[i][1] = dp[i-1][1]
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        return max(dp[-1][0], dp[-1][1])