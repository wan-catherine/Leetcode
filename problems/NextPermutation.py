class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        max = nums[len(nums) - 1]
        k = -1
        for index in range(len(nums) -2, -1, -1):
            if nums[index] >= max:
                max = nums[index]
                continue

            k = index + 1
            i = len(nums) - 1
            while k < len(nums):
                if nums[index] < nums[k]:
                    k += 1
                else:
                    i = k - 1
                    break
            nums[index], nums[i] = nums[i], nums[index]
            nums[index + 1:] = sorted(nums[index + 1:])
            break
        if k == -1:
            nums.reverse()
        return nums