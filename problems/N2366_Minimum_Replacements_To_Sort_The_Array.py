import math
from typing import List

"""
if nums[i] > prev,then we try to split nums[i] into x part, each part is prev . 
The last part might be less than prev . So we need to do math.ceil or (nums[i] + prev - 1) // prev 
k = math.ceil(nums[i]/prev)
so we have k parts here. It needs k-1 operations. 

How to decide the current prev is the key part !
prev = nums[i] // k 

When I first try , I think this example [3,9,8] 
the greedy thought is split 9 into [8,1], but then 1 will cause 3 to do split . 
so [4,5] will be better . 

prev = nums[i] // k , this way actually we split into 2 , and when nums[i] //k , we will do our best to make 
each part as equal to each other as possible. 
"""

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res, prev = 0, nums[-1]
        length = len(nums)
        for i in range(length - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                k = math.ceil(nums[i] / prev)
                res += k - 1
                prev = nums[i] // k
        return res