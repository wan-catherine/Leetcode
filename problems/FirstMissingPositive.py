class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 1:
            return 1

        for i in range(length):
            while (nums[i] > 0 and nums[i] <= length):
                j = nums[i] - 1
                if (nums[i] != nums[j]):
                    nums[i], nums[j] = nums[j],nums[i]
                else:
                    break

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1

