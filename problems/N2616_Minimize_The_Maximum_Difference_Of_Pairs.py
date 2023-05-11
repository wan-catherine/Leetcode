from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        length = len(nums)
        def count(m):
            i = 0
            res = 0
            while i + 1 < length:
                if nums[i+1] - nums[i] <= m:
                    res += 1
                    i += 2
                else:
                    i += 1
            return res
        l, r = 0, nums[-1] - nums[0] + 1
        while l < r:
            mid = (r - l) // 2 + l
            if count(mid) >= p:
                r = mid
            else:
                l = mid + 1
        return l
