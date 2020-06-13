"""
DP
dp[i] means for ith number , when it includes , the number of largest divisible subset .
We first sort the nums , so we can know if a number n % res[-1] , then it can add in this result set .

so dp[i] is related to all the previous days 1,,,i-1 which nums[i] % res[-1] == 0 and choose the largest one .

Because, we need to give the real subset , so we need to track the previous index for ith number .
After we can the largest divisible subset and it's index, then we can backtrack all it's previous index
then to create the largest divisible subset.

This is a new category for DP . before dp[i] only related to dp[i-1] or dp[i-2]
But here it related to all status before it dp[1...i-1]

Time complexity: O(n*n)
"""
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums = sorted(nums)
        nums_len = len(nums)
        dp = [1] * nums_len
        previous = [-1] * nums_len
        for i in range(nums_len):
            for j in range(i):
                if not nums[i] % nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == dp[j] + 1:
                        previous[i] = j
        max_count = 0
        final_index = -1
        for i in range(nums_len):
            max_count = max(max_count, dp[i])
            if max_count == dp[i]:
                final_index = i
        res = set()
        while final_index != -1:
            res.add(nums[final_index])
            final_index = previous[final_index]
        return res
