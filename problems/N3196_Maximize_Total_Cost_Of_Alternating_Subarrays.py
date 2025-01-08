import sys
from typing import List

'''
I think it should be DP , but think it as n*n 
Actually , the ith flip or not only depends the previous :
    if i - 1 flip , then i can't flip 
    if i - 1 not flip , then i can flip or not flip 
'''

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [[0, 0] for _ in range(length)]
        dp[0][0] = nums[0]
        dp[0][1] = -sys.maxsize
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + nums[i]
            dp[i][1] = dp[i - 1][0] - nums[i]
        return max(dp[-1])