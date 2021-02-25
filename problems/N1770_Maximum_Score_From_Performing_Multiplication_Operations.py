import sys


class Solution(object):
    def maximumScore_TLE(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        memo = {}

        def helper(l, r, index, cur):
            if (l, r, index, cur) in memo:
                return memo[(l, r, index, cur)]
            if index == len(multipliers):
                return cur
            temp = max(helper(l+1, r, index+1, cur + multipliers[index] * nums[l])
                       , helper(l, r-1, index+1, cur + multipliers[index]*nums[r]))
            memo[(l, r, index, cur)] = temp
            return temp
        return helper(0, len(nums)-1, 0, 0)

    """
    DP : Interval DP 
    dp[i][j] : get i elements from the head of nums and get j elements from the end of nums, then the largest result.
    Interval Dp , two loops
    First : length 
    second : start point 
    """
    def maximumScore(self, nums, multipliers):
        nums = [0] + nums
        multipliers = [0] + multipliers
        length = len(multipliers)
        dp = [[-sys.maxsize] * length for _ in range(length)]
        dp[0][0] = 0
        res = -sys.maxsize
        for l in range(1, length):
            for i in range(l+1):
                j = l - i
                if i >= 1:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + multipliers[l] * nums[i])
                if j >= 1:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + multipliers[l] * nums[-j])
                if l == length - 1:
                    res = max(res, dp[i][j])
        return res


