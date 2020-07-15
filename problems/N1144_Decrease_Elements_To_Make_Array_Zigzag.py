class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        nums_1 = nums[:]
        res = 0
        for i in range(0,length, 2):
            if i - 1 >= 0 and nums[i-1] <= nums[i]:
                res += nums[i] - nums[i-1] + 1
                nums[i] = nums[i - 1] - 1
            if i + 1 < length and nums[i + 1] <= nums[i]:
                res += nums[i] - nums[i+1] + 1
                nums[i] = nums[i + 1] - 1

        res_1 = 0
        for i in range(1,length, 2):
            if i - 1 >= 0 and nums_1[i-1] <= nums_1[i]:
                res_1 += nums_1[i] - nums_1[i-1] + 1
                nums_1[i] = nums_1[i - 1] - 1
            if i + 1 < length and nums_1[i + 1] <= nums_1[i]:
                res_1 += nums_1[i] - nums_1[i+1] + 1
                nums_1[i] = nums_1[i + 1] - 1
        return min(res, res_1)
