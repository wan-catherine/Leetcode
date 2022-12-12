import collections
from typing import List

"""
This can transfer to -1(n < k), 0(n==k), 1(n > k) 

Two points:
1. 
    No need to consider the index of k . 
    because :
        a. odd subarray which without 0, sum of it won't be 0
        b. even subarray which with out 0 , sum of it won't be 1
        
2. 
    need to sub presum_even[0] = 1 , which means there is 1 for empty subarray's sum == 0
    
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        array = []
        for i, n in enumerate(nums):
            if n == k:
                array.append(0)
            elif n < k:
                array.append(-1)
            else:
                array.append(1)
        presum_odd, presum_even = collections.defaultdict(int), collections.defaultdict(int)
        prev = 0
        res = 0
        presum_even[0] = 1
        for i in range(length):
            prev += array[i]
            if i % 2:
                res += presum_even[prev-1]
                res += presum_odd[prev]
                presum_even[prev] += 1
            else:
                res += presum_odd[prev - 1]
                res += presum_even[prev]
                presum_odd[prev] += 1
        return res

