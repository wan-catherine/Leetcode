from typing import List
"""
DP problem:
zero: at index i, how many 0..0 subsequence. 
one : at index i, how many 0..1..1 subsequence
two : at index i, how many 0..1..2..2 subsequece

Here we need to notice how set to initial value to zero/one/two. 
zero, one, two = 1, 0, 0
 
but when we first meet '0', then according to zero = 2 * zero, it will be 2 : [], [0]. 
So when we cacluate one, we need to minus 1 : one = zero - 1 + 2 * one
"""

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        length = len(nums)
        zero, one, two = 1, 0, 0
        for i in range(length):
            if nums[i] == 0:
                zero = 2 * zero
            elif nums[i] == 1:
                one = zero - 1 + 2 * one
            else:
                two = one + 2 * two
        return two % (10**9+7)