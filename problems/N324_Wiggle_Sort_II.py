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
        snums = sorted(nums, reverse=True)
        i, length = 0, len(nums)

        for j in range(1, length, 2):
            nums[j] = snums[i]
            i += 1
        for j in range(0, length, 2):
            nums[j] = snums[i]
            i += 1

