from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ones = [0] * 30
        res, length = [], len(nums)
        for idx in range(length-1, -1, -1):
            for i in range(31, -1, -1):
                if nums[idx] & (1 << i):
                    ones[i] = idx
            res.append(max(1, max(ones) - idx + 1))
        return res[::-1]

