"""
If we already cover [1, m], then if there is a number: num in nums which num < m,
then it can cover [1, m+n]
If num > m , then we need to patch m+1 which will cover [1, 2*m+1].
"""
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patch = 0
        i, length = 0, len(nums)
        res = 0
        while patch < n:
            if i < length and patch + 1 >= nums[i]:
                patch += nums[i]
                i += 1
            else:
                res += 1
                patch += patch + 1
        return res

        
