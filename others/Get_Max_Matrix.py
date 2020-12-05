import sys


class Solution(object):
    def getMaxMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(matrix), len(matrix[0])
        res = [0,0,0,0]
        ans = matrix[0][0]
        for up in range(rows):
            arr = [0]*cols
            for down in range(up, rows):
                for j in range(cols):
                    arr[j] += matrix[down][j]
                dp = [[arr[0],0] for _ in range(cols)]
                for i in range(1, cols):
                    if arr[i] + dp[i-1][0] > arr[i]:
                        dp[i] = [arr[i] + dp[i-1][0], dp[i-1][1]]
                    else:
                        dp[i] = [arr[i], i]
                    if dp[i][0] > ans:
                        ans = dp[i][0]
                        res = [up,dp[i][1],down,i]
        return res