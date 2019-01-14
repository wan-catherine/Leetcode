class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        l = len(nums)
        i = 0
        j = 1
        res = []
        while j < l:
            if nums[i] == nums[j]:
                i += 2
                j += 2
            else:
                res.append(nums[i])
                i += 1
                j += 1
        if len(res) < 2:
            res.append(nums[i])
        return res