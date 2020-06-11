"""
So for this problem, we can see this way . First ,we know the first and last house can't be rob together .
so we have two situation :
    1. we ingore the last house , for hours[0:last-1]
    2, we ingore the first hours, for hours[1:last}
Those two situations are same as #198.
Then we max(#1, #2)
"""
class Solution:
    def rob_before(self, nums):
        if nums == None or len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        start = self.dp(nums[0:len(nums)-1])
        end = self.dp(nums[1:])
        return max(start, end)


    def dp(self, nums):
        res = [0] * (len(nums) + 1)
        res[1] = nums[0]
        i = 2
        while i <= len(nums):
            res[i] = max(res[i-2] + nums[i-1], res[i - 1])
            i += 1
        return res[-1]

    def rob_help(self, nums):
        if not nums:
            return 0
        nums_len = len(nums)
        dp = [[0]* nums_len, [0]* nums_len]
        dp[1][0] = nums[0]
        for i in range(1, nums_len):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1])
            dp[1][i] = dp[0][i-1] + nums[i]
        return max(dp[0][-1], dp[1][-1])

    def rob(self, nums):
        if not nums:
            return 0
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        ignore_fist = self.rob_help(nums[1:])
        ignore_last = self.rob_help(nums[:nums_len-1])
        return max(ignore_fist, ignore_last)
