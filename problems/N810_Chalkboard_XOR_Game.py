from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        ans = 0
        for n in nums:
            ans ^= n
        if ans == 0:
            return True
        length = len(nums)
        if length % 2:
            return False
        return True
