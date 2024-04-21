from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        length = len(nums)
        res = 0
        nums.sort()
        i, l, r = 0, length - 1, length - 1
        while i < length:
            while r > i and nums[i] + nums[r] > upper:
                r -= 1
            if r == i:
                break
            while l > i and nums[i] + nums[l] >= lower:
                l -= 1
            if l == length:
                break
            l = max(l, i)
            res += (r - l) if r >= l else 0
            i += 1
        return res