class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return None
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            i += 1
        if nums[i] > nums[i-1]:
            return i