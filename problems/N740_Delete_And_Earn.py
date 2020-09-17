class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maximum = max(nums)
        arr = [0] * (maximum + 1)
        for n in nums:
            arr[n] += n
        dp = [0] * (maximum + 1)
        dp[1] = arr[1]
        res = arr[1]
        for i in range(2, (maximum + 1)):
            dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            res = max(dp[i], res)
        return res
