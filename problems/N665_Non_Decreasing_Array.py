class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length == 1:
            return True
        count = 0 if nums[1] >= nums[0] else 1
        prev = nums[1]
        for i in range(2, length):
            if nums[i] < prev:
                if nums[i] >= nums[i-2]:
                    prev = nums[i]
                count += 1
                if count > 1:
                    return False
            else:
                prev = nums[i]
        return True

