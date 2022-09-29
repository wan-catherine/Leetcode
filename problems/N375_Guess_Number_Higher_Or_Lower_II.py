from math import inf

"""
DP
for [1,2,3,4,5] 
    1. guess 1, []   [2,3,4,5]
    2. guess 2, [1]  [3,4,5]
    3. guess 3, [1,2] [4,5]
    4. guess 4, [1,2,3] [5]
    5. guess 5, [1,2,3,4] []
    
Then for the result , we will get the minimum of all those 5 situations. 

"""

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # set length here equals to n+2 , because k can be n+1 (len = 2, j = n + 1)
        #  dp[k+1][j] : maybe [6,5] ：  guess 5, [1,2,3,4] []
        dp = [[0]*(n+2) for _ in range(n+2)]

        for len in range(2, n+1):
            for i in range(1, n - len + 2):
                j = i + len - 1
                dp[i][j] = float(inf)
                for k in range(i, j+1):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))

        return dp[1][n]