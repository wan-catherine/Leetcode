from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        length = len(nums)
        diff = [0] * length
        cur = 0
        for i in range(length-1):
            cur += diff[i]
            if cur > nums[i]:
                return False
            delta = nums[i] - cur
            diff[i] += delta
            if i + k < length:
                diff[i+k] -= delta
            cur += delta
        return cur + diff[-1] == nums[-1]
