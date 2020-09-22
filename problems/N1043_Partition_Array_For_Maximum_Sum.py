class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        length = len(arr)
        dp = [0] * (length + 1)
        for i in range(1, length+1):
            val = 0
            for l in range(1, k+1):
                if i - l < 0:
                    continue
                j = i - l
                val = max(val, arr[j])
                dp[i] = max(dp[i], dp[j] + l*(val))
        return dp[-1]