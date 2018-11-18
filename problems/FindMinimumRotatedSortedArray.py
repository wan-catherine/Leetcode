class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) < 1:
            return None

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                return nums[i]
            i += 1