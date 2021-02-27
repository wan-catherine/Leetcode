class Solution(object):
    def largestSumOfAverages_dfs(self, A, K):
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

    """
    dp[i][j] : the largest score we can get by splitting arr[i:] into j groups. 
    dp[i][j] = max(dp[i][j], dp[k][j-1]) k is the index for arr[i+1:]
    """
    def largestSumOfAverages(self, arr, K: int) -> float:
        length = len(arr)
        prefix = [0] + arr[:]
        for i in range(1, length):
            prefix[i + 1] += prefix[i]

        dp = [[0] * (K+1) for _ in range(length)]
        for i in range(length):
            dp[i][1] = (prefix[-1] - prefix[i]) / (length - i)

        for i in range(length - 1, -1, -1):
            for j in range(2, min(length - i, K) + 1):
                for k in range(i + 1, length - j + 2):
                    dp[i][j] = max(dp[i][j], dp[k][j - 1] + (prefix[k] - prefix[i]) / (k - i))

        return max(dp[0])