class Solution(object):
    def wiggleSort_nlgn(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        nums_len = len(nums)
        p, q = (nums_len - 1) // 2, nums_len - 1
        for i in range(nums_len):
            if i % 2:
                nums[i] = sorted_nums[q]
                q -= 1
            else:
                nums[i] = sorted_nums[p]
                p -= 1
        print(nums)
        return nums

    def wiggleSort(self, nums):
        nums_len = len(nums)
        for i in range(nums_len-1):
            is_even = False if i % 2 else True
            if (is_even and nums[i] > nums[i+1]) or (not is_even and nums[i] < nums[i+1]):
                nums[i],nums[i+1] = nums[i+1],nums[i]
        print(nums)
        return nums



