import bisect
"""
from right to left , to find the right position to insert the number . 
We can use binary search to find this position . 
Here I use python module to do so . 

We can write binary search by ourself, but need to deal with duplicated number.
"""

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums

        nums_len = len(nums)
        res = [0] * nums_len
        temp = [nums[-1]]
        for i in range(nums_len-2, -1, -1):
            index = bisect.bisect_left(temp,nums[i])
            bisect.insort_left(temp, nums[i])
            res[i] = index
        return res