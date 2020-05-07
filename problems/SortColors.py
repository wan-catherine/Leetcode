class Solution:
    def sortColors_old(self, nums):
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

    # it's a 3-way partitioning of quicksort
    # here we can't make sure the first element is the middle number : 1,
    # so I insert number 1 in the index:0 of the list
    # notice : can't use nums = [1] + nums to add 1
    # because this actually create a new nums by copying 1 and all elements in original nums
    # you can check id(nums) before and after to see the memory address changed

    def sortColors(self, nums):
        gt = len(nums)
        nums.insert(0,1)
        lo = 0
        i = 1
        while i <= gt:
            if nums[i] < nums[lo]:
                nums[i], nums[lo] = nums[lo], nums[i]
                i += 1
                lo += 1
            elif nums[i] > nums[lo]:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        del nums[lo]

