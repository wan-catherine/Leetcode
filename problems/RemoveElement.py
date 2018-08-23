class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0

        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)