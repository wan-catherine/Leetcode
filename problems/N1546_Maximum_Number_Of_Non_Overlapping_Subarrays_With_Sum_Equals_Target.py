"""
If the problem mension something like : subarrays, it will give a strong hint that it might use prefix sum method.

This problem has no different. It uses prefix sum and hash table.

But the key point is how to get non-overlapping subarrays. It's smiliar as greedy.
In order to get as many as subarrays possible, we first need to make sure all subarray as short as possible.

So when we first get some subarray, we will count it : res += 1.
Then we need to reset the prefix sum and hash table. To treat the left array like a brand new array to get the subarray.
This way we can make sure those subarrays don't overlapping at all!!!

"""
class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        res = 0
        prefix_set = {0}
        prefix_sum = 0
        for i in range(length):
            prefix_sum += nums[i]
            if prefix_sum - target in prefix_set:
                res += 1
                prefix_sum = 0
                prefix_set = {0}
            else:
                prefix_set.add(prefix_sum)
        return res