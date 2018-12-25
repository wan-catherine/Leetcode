class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) < 2:
            return

        i = 0
        j = 1
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                j += 1
            else:
                while j < len(nums):
                    if nums[j] == 0:
                        j += 1
                        continue
                    nums[i] = nums[j]
                    nums[j] = 0
                    j += 1
                    break
                i += 1
