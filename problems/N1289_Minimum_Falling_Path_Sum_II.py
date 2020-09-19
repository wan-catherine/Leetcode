"""
Two key points :
1. get the first and second minimum values of a row. In case there is duplicated value in the row, so need to check the first minimum's index
2. dp[i][j] : the minimum sum of a falling path with non-zero shifts which ends at jth col.
    dp[i][j] = min(dp[i][col!=j]) + arr[i][j]
    so we can check dp[i-1]'s first and second minimum values. If min(dp[i-1]) == dp[i-1][j] , we will use the second minimum. If not ,
    will use the first minimum value.
"""
class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        def two_minimum(row):
            first = 100 * 200
            f_index = 0
            for i, n in enumerate(row):
                if first > n:
                    first = n
                    f_index = i
            second = 100 * 200
            for i, n in enumerate(row):
                if i == f_index:
                    continue
                second = min(second, n)
            return (first, second, f_index)

        n = len(arr)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = arr[0][i]

        for i in range(1, n):
            first, second, f_index = two_minimum(dp[i-1])
            for j in range(n):
                if j != f_index:
                    dp[i][j] = arr[i][j] + first
                else:
                    dp[i][j] = arr[i][j] + second

        # print(dp)
        return min(dp[-1])