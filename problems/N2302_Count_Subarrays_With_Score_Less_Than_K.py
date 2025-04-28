from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        prefix = [0] + nums[:]
        for i in range(length):
            prefix[i+1] += prefix[i]

        res = 0
        j = 0
        for i in range(length):
            while j < length and (prefix[j+1] - prefix[i]) * (j - i + 1) < k:
                j += 1
            res += j - i
        return res
