"""
First I think it needs a monotonic stack to maintain the maximum value of a subarray.
Then I found when A[i] > R , we need to clear this stack , so it seems we don't need to maintain it anyway.

This is a DP problem:
dp[i+1] means the number of subarrays which each subarray includes A[i] satisfied the condition
Three situations:
    1. A[i] > R : dp[i+1] = 0
    2. R >= A[i] >= L : dp[i+1] = i - start + 1 (start is the index which first satisfied the condition
    3. A[i] < L : so it can be follow a good subarray dp[i+1] = dp[i]

"""
from typing import List


class Solution(object):
    def numSubarrayBoundedMax_dp(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        length = len(A)
        dp = [0]*(length+1)
        start = -1
        res = 0
        for i in range(length):
            if A[i] > R:
                start = -1
                dp[i+1] = 0
                continue
            if start == -1:
                start = i
            if A[i] >= L and A[i] <= R:
                dp[i+1] = i - start + 1
            else:
                dp[i+1] = dp[i]
            res += dp[i+1]
        return res

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        length = len(nums)
        stack = []
        res = 0
        def helper(arr):
            l = len(arr)
            ans = (l + 1) * l // 2
            n = 0
            for i, c in enumerate(arr):
                if c >= left:
                    ans -= (n + 1) * n // 2
                    n = 0
                    continue
                n += 1
                if i == l - 1:
                    ans -= (n + 1) * n // 2
            return ans
        for i in range(length):
            if nums[i] > right:
                res += helper(stack)
                stack.clear()
                continue
            stack.append(nums[i])
            if i == length - 1:
                res += helper(stack)
        return res
