"""
There are two status :
    0 : non-rob
    1: rob

so for each house we have two choice 0 or 1.
For ith house
    if we don't rob : d[0][i] = max(dp[0][i-1], dp[1][i-1]
    for yesterday , we can rob and non-rob , get the maximum

    if we rob : d[1][i] = dp[0][i-1] + nums[i]
    for yesterday, we can only non-rob

"""
class Solution(object):
    def rob_before(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) < 1:
            return 0

        res = [0] * (len(nums) + 1)
        res[1] = nums[0]
        i = 2
        while i <= len(nums):
            res[i] = max(res[i-2] + nums[i-1], res[i - 1])
            i += 1
        print(res)
        return res[-1]

    def rob(self, nums):
        if not nums:
            return 0
        nums_len = len(nums)
        dp = [[0]* nums_len, [0]* nums_len]
        dp[1][0] = nums[0]
        for i in range(1, nums_len):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1])
            dp[1][i] = dp[0][i-1] + nums[i]
        return max(dp[0][-1], dp[1][-1])