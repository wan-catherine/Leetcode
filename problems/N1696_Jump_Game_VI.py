import bisect
from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        stack = deque()
        stack.append(0)
        for i in range(1, length):
            while stack and i - stack[0] > k:
                stack.popleft()
            dp[i] = nums[i] + dp[stack[0]]
            while stack and dp[stack[-1]] < dp[i]:
                stack.pop()
            stack.append(i)
        return dp[-1]