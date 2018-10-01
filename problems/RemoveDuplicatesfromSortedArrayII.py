class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1

        num = 0
        dup = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                dup += 1
            else:
                num += dup - 2 if dup - 2 > 0 else 0
                dup = 1
            nums[i - num] = nums[i]

        num += dup - 2 if dup - 2 > 0 else 0
        nums[len(nums) - 1 - num] = nums[len(nums) - 1]
        length = len(nums) - num
        nums = nums[0:length]
        return length