from typing import List

"""
dp[i] : left i stones, the maximum diff between the first and second player .
    1. i == 1, there are only one stone, so the diff = 0
    2. i == 2, for the first player, there is only one option: pick up all two stones , then for the second player, 
        it becomes 1 stone. so the diff = prefix[n-1] = prfix[n-1] - dp[1]
    3. i == 3, for the first player , there are two options : 
        a. pick all 3 stones and left 1 for the second player: diff = prefix[n-1] - dp[1] == dp[2]
        b. pick the left 2 stones and left 2 for the second player : diff = prefix[n-2] - dp[2]
    4. i in general , diff = max(dp[i-1], prefix[n-i+1] - dp[i-1])   
"""

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        length = len(stones)
        dp = [0] * (length + 1)
        prefix = stones[:]
        for i in range(1, length):
            prefix[i] += prefix[i-1]
        dp[2] = prefix[length - 1] - dp[1]
        for i in range(3, length + 1):
            dp[i] = max(dp[i-1], prefix[length - i + 1] - dp[i-1])
        return dp[length]

