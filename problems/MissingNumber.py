class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        nums = sorted(nums)
        for j in nums:
            if j == i:
                i += 1
            else:
                return i
        return i

    def missingNumber_effective(self, nums):
        # Arithmetic progression sum
        n = len(nums) + 1
        return int((0 + n - 1)*n/2 - sum(nums))