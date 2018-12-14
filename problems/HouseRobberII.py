class Solution:
    def rob(self, nums):
        if nums == None or len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        start = self.dp(nums[0:len(nums)-1])
        end = self.dp(nums[1:])
        return max(start, end)


    def dp(self, nums):
        res = [0] * (len(nums) + 1)
        res[1] = nums[0]
        i = 2
        while i <= len(nums):
            res[i] = max(res[i-2] + nums[i-1], res[i - 1])
            i += 1
        return res[-1]