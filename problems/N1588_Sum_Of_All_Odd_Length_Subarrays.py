from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        res = 0
        for i, v in enumerate(arr):
            left, right = i, length - i - 1
            left_odd = (left + 1) // 2
            left_even = left // 2 + 1
            right_odd = (right + 1) // 2
            right_even = right // 2 + 1
            res += v * (left_odd * right_odd + left_even * right_even)
        return res