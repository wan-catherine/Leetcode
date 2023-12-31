import sys
from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        length = len(nums)
        nums = [-sys.maxsize] + nums + [sys.maxsize]
        l, r = 1, length
        while l <= length:
            if nums[l] < nums[l + 1]:
                l += 1
            else:
                break
        while r >= 1:
            if nums[r] > nums[r - 1]:
                r -= 1
            else:
                break

        if r < l:
            return length * (length - 1) // 2 + length

        res = 0
        j = length + 1
        for i in range(l, -1, -1):
            while j >= r and nums[j] > nums[i]:
                j -= 1
            res += length + 1 - j
        return res