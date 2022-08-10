from typing import List
"""
Key point : 
    The maximum bitwise-OR is the bitwise-OR of the whole array.
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        length = len(nums)
        memo = {}
        val = 0
        for n in nums:
            val |= n

        def dfs(index, cur):
            nonlocal val
            if (index, cur) in memo:
                return memo[(index, cur)]
            ans = 0
            if cur == val:
                ans += 1

            for i in range(index, length):
                v = cur
                v |= nums[i]
                ans += dfs(i + 1, v)
            memo[(index, cur)] = ans
            return ans

        return dfs(0, 0)