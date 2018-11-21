class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) < 1:
            return 0

        res = [0] * (len(nums) + 1)
        res[1] = nums[0]
        i = 2
        while i <= len(nums):
            res[i] = max(res[i-2] + nums[i-1], res[i - 1])
            i += 1
        print(res)
        return res[-1]