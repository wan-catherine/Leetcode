"""
Amazing way to deal with the intervals!!!
Where there is an interval [i, j] , set i as 1, then set j+1 as -1.
When you enter the interval, it will be added one, but when you out of the interval you need to minus one to keep it same as before.
"""
class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        length = len(nums)
        count = [0] * (length + 1)
        for i, j in requests:
            count[i] += 1
            count[j+1] -= 1

        for i in range(1, length+1):
            count[i] += count[i-1]

        nums.sort(reverse=True)
        count.sort(reverse=True)
        res = 0
        for i in range(length):
            res += count[i] * nums[i]
        return res % (10**9 + 7)
