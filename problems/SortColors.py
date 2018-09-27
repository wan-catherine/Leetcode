class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) < 2:
            return

        i = 0
        j = 0
        k = 0
        for n in nums:
            if n == 0:
                i += 1
            elif n == 1:
                j += 1
            else:
                k += 1

        p = 0
        while p < len(nums):
            if p < i:
                nums[p] = 0
            elif p < j + i:
                nums[p] = 1
            else:
                nums[p] = 2
            p += 1

