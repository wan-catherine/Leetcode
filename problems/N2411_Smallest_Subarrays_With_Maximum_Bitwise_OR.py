from typing import List


class Solution:
    def smallestSubarrays_before(self, nums: List[int]) -> List[int]:
        ones = [0] * 30
        res, length = [], len(nums)
        for idx in range(length-1, -1, -1):
            for i in range(31, -1, -1):
                if nums[idx] & (1 << i):
                    ones[i] = idx
            res.append(max(1, max(ones) - idx + 1))
        return res[::-1]

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ones = [0] * 32
        res, length = [], len(nums)
        j = length - 1
        def check(j):
            for i in range(32):
                if ones[i] == 1 and nums[j] & (1 << i):
                    return False
            return True

        for idx in range(length - 1, -1, -1):
            for i in range(32):
                if nums[idx] & (1 << i):
                    ones[i] += 1
            while j > idx and check(j):
                for i in range(32):
                    if nums[j] & (1 << i):
                        ones[i] -= 1
                j -= 1
            res.append(j - idx + 1)
        return res[::-1]