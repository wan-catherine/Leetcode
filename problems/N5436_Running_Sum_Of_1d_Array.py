class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        nums_len = len(nums)
        res = [nums[0]] * nums_len
        for i in range(1, nums_len):
            res[i] = res[i-1] + nums[i]
        return res