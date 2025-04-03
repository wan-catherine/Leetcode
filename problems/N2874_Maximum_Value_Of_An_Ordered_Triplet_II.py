from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        length = len(nums)
        suff = nums[:]
        for i in range(length - 2, -1, -1):
            suff[i] = max(nums[i], suff[i + 1])

        res = 0
        l = 0
        for i in range(1, length-1):
            if nums[i] < nums[l]:
                res = max(res, (nums[l] - nums[i]) * suff[i+1])
            else:
                l = i
        return res