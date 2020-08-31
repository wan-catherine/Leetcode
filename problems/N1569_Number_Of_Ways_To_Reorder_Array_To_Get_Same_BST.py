"""
Key point :
how to get the left and right.
left = [i for i in nums if i < root]
right = [i for i in nums if i > root]

we need to keep left and right same order seperately.
"""
class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = self.helper(nums)
        return (count - 1) % (10**9 + 7)

    def helper(self, nums):
        length = len(nums)
        if length in [0,1,2]:
            return 1
        if length == 3:
            if (nums[0] > nums[1] and nums[0] < nums[2]) or (nums[0] < nums[1] and nums[0] > nums[2]):
                return 2
            else:
                return 1
        root = nums[0]
        left = [i for i in nums if i < root]
        right = [i for i in nums if i > root]
        count = 1
        for i in range(1, length):
            count *= i
        left_len, right_len = len(left), len(right)
        count = count * self.helper(left)*self.helper(right)
        for i in range(1, left_len+1):
            count //=i
        for i in range(1, right_len + 1):
            count //= i
        return count



