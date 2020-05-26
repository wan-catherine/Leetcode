import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.nums_len = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = []
        for i in range(self.nums_len):
            if self.nums[i] == target:
                index.append(i)
        if len(index) == 1:
            return index[0]

        # reserviov sampling algorithm
        res = index[0]
        for j in range(1,len(index)):
            r = random.randint(0,j)
            if r == 0:
                res = index[j]
        return res
