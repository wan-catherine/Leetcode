import bisect
from math import inf
from typing import List

from sortedcontainers import SortedSet


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        length = len(nums)
        arr = []
        for i in range(length):
            arr.append(nums[i] - i)
        dp = {}
        keys = SortedSet()
        res = -inf
        for i in range(length):
            ans = nums[i]
            index = keys.bisect_right(arr[i]) - 1
            if index >= 0:
                ans = max(nums[i], nums[i] + dp[keys[index]], dp[keys[index]])

            while index + 1 < len(keys) and dp[keys[index + 1]] < ans:
                del keys[index + 1]

            keys.add(arr[i])
            dp[arr[i]] = ans
            res = max(res, ans)
        return res

