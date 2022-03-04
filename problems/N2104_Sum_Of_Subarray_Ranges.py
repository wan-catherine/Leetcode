from typing import List
"""
Monotonic stack to get the previous (max/min) and next (max/min). 
Here is a key point : 
[1, 3, 3], in one subarray, there are multiple max/min , in order to avoid duplicate calculation 
we need to use [ ) or ( ]. 
    1. For min, we can define the rightest is the min . 
    2. For max, we can define the rightest is the max . 
    
    or we can define the leftest is max/min.

"""

class Solution:
    def subArrayRanges_n_2(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0

        for i in range(1, length):
            l, s = nums[i], nums[i]
            for j in range(i - 1, -1, -1):
                l = max(l, nums[j])
                s = min(s, nums[j])
                res += l - s
        return res

    def subArrayRanges(self, nums: List[int]) -> int:
        length = len(nums)
        stack, maxl, maxr = [], [-1] * length, [length] * length
        for i in range(length-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                idx = stack.pop()
                maxl[idx] = i
            stack.append(i)
        stack = []
        for i in range(length):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                maxr[idx] = i
            stack.append(i)
        stack, minl, minr = [], [-1] * length, [length] * length
        for i in range(length - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                idx = stack.pop()
                minl[idx] = i
            stack.append(i)
        stack = []
        for i in range(length):
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                minr[idx] = i
            stack.append(i)
        res = 0
        for i in range(length):
            res += (i - maxl[i]) * (maxr[i] - i) * nums[i]
            res -= (i - minl[i]) * (minr[i] - i) * nums[i]
        return res