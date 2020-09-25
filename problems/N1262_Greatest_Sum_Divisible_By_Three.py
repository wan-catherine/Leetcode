class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [[0]*3 for _ in range(length)]
        dp[0][nums[0]%3] = nums[0]

        for i in range(1, length):
            val = nums[i] % 3
            if val == 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i])
                dp[i][1] = max(dp[i-1][1], (dp[i-1][1] + nums[i]) if dp[i-1][1] > 0 else 0)
                dp[i][2] = max(dp[i-1][2], (dp[i-1][2] + nums[i]) if dp[i-1][2] > 0 else 0)
            elif val == 1:
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i])
                dp[i][2] = max(dp[i-1][2], (dp[i-1][1] + nums[i]) if dp[i-1][1] > 0 else 0)
                dp[i][0] = max(dp[i-1][0], (dp[i-1][2] + nums[i]) if dp[i-1][2] > 0 else 0)
            elif val == 2:
                dp[i][0] = max(dp[i-1][0], (dp[i-1][1] + nums[i]) if dp[i-1][1] > 0 else 0)
                dp[i][1] = max(dp[i-1][1], (dp[i-1][2] + nums[i]) if dp[i-1][2] > 0 else 0)
                dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i])
        # print(dp)
        return dp[-1][0]
