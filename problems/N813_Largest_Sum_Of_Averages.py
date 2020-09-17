class Solution(object):
    def largestSumOfAverages(self, A, K):
        memo = {}
        length = len(A)

        def dfs(start, k):
            if (start, k) in memo:
                return memo[(start, k)]
            if k == 1:
                memo[(start, k)] = sum(A[start:]) / (length - start)
                return memo[(start, k)]
            if start >= length:
                return 0

            value = 0
            for i in range(start + 1, length):
                val = sum(A[start:i]) / (i - start)
                value = max(value, dfs(i, k - 1) + val)
            memo[(start, k)] = value
            return value

        return dfs(0, K)