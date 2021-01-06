"""
LIS problem: longest increasing sebsequence

Here we treat the whole column as a whole , then use dp to get the LIS.
LIS :
    the simple number [1,4,2, 5,3], it can use greedy : O(NlogN).
    the complexity compare like this problem(need to compare whole column), so use DP : O(N**2)
"""
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        dp = [1] * cols

        def check(x, y):
            for i in range(rows):
                if A[i][x] < A[i][y]:
                    return False
            return True

        for i in range(cols):
            for j in range(i):
                if check(i, j):
                    dp[i] = max(dp[i], dp[j] + 1)

        return cols - max(dp)
