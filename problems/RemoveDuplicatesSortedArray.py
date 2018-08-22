class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] :
            return 0

        if len(nums) < 2:
            return 1

        i = 1
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                del nums[i - 1]
            else:
                i += 1
        return len(nums)

