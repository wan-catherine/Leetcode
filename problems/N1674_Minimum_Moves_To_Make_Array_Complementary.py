import collections

"""
A good problem. 
We can know the range of nums[i] + nums[length-i-1] is [2, max(ssum)]. 
We can move length steps (move all to 1) to make the array complementary. 
When nums[i] + nums[length-i-1] == T , then zero move. 
When nums[i] + nums[length-i-1] is [left, right+1), then one move. 
"""
class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        ssum = collections.defaultdict(int)
        diff = collections.defaultdict(int)
        length = len(nums)
        for i in range(length//2):
            a, b = nums[i], nums[length-i-1]
            mmin, mmax = min(a,b), max(a, b)
            left, right = mmin + 1, mmax + limit  # in [left, right+1), we can only move one step.
            diff[left] -= 1
            diff[right+1] += 1
            ssum[a+b] += 1

        cur, res = length, length
        for t in range(2, max(ssum) + 1):
            cur += diff[t]
            res = min(res, cur - ssum[t])
        return res
