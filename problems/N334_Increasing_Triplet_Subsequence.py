"""
Notice here one and two can be zero.
So we can't use 'not one/two' to check if it's None
"""
import sys
from typing import List


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one, two = None, None
        for i in nums:
            if one == None:
                one = i
                continue

            if two != None and i > two:
                return True

            if one != None and i > one:
                two = i if two == None else min(i, two)
                continue
            if one > i:
                one = i
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        one, two = sys.maxsize, sys.maxsize
        for i in range(length):
            if nums[i] > two:
                return True
            if nums[i] > one:
                two = nums[i]
            else:
                one = nums[i]
        return False

