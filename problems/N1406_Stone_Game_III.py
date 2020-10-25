import sys
"""
dp[i] : ignore the first i piles, the maximum scores which the current player can get . 
dp[i] has three situations:
    1. get the (i+1)th pile
    2. get the (i+1, i+2)th piles
    3. get the (i+1, i+2, i+3)th piles
    
 then the opponent player can get : dp[i+1], dp[i+2], dp[i+3]
 the current player can get sum[i+k:n] - dp[i+k] (k is [1,2,3]
"""

class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        length = len(stoneValue)
        dp = [-sys.maxsize] * (length + 1)
        dp[length] = 0
        presum = stoneValue[:]
        for i in range(1, length):
            presum[i] += presum[i-1]

        for i in range(length-1, -1, -1):
            temp = 0
            for j in range(1, 4):
                if i + j > length:
                    break
                temp += stoneValue[i+j-1]
                dp[i] = max(dp[i], temp + presum[-1] - presum[i+j-1] - dp[i+j])

        if dp[0] > presum[-1] - dp[0]:
            return 'Alice'
        if dp[0] < presum[-1] - dp[0]:
            return 'Bob'
        return 'Tie'