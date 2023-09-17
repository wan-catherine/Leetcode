from typing import List


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        for i in range(length):
            sarr = set()
            prev = -1
            for j in range(i, length):
                if nums[j] not in sarr:
                    prev += 1
                    if nums[j] + 1 in sarr:
                        prev -= 1
                    if nums[j] - 1 in sarr:
                        prev -= 1
                    sarr.add(nums[j])
                res += prev
        return res