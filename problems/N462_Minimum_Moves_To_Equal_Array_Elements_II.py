"""
The median minimizes the sum of absolute deviations (the ℓ1 norm)
https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm

"""
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        res = 0
        nums.sort()
        median = nums[length // 2]
        for i in nums:
            res += abs(i - median)
        return res