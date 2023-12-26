import bisect
from typing import List


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        nums = [0] + nums
        length = len(nums)
        dp = [0] * length
        le = [0] * length
        prev = [0] * length
        for i in range(1, length):
            prev[i] = prev[i-1] + nums[i]

        stack = [(0,0)]
        for i in range(1, length):
            idx = bisect.bisect_right(stack, (prev[i],length))
            idx -= 1

            j = stack[idx][1]
            le[i] = le[j] + 1
            dp[i] = prev[i] - prev[j]

            val = dp[i] + prev[i]
            while stack and stack[-1][0] >= val:
                stack.pop()
            stack.append((val, i))
        # print(le)
        return le[-1]



