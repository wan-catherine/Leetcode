import math
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        length = len(nums)
        stack = []
        def check(a, b):
            return math.gcd(a, b) > 1

        def cal(a, b):
            return a * b // math.gcd(a, b)

        for i in range(length):
            if not stack:
                stack.append(nums[i])
                continue
            v = nums[i]
            while stack and check(stack[-1], v):
                val = stack.pop()
                v = cal(v, val)
            stack.append(v)
        return stack
