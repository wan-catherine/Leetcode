class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        length = len(stones)
        stones = [0] + stones
        dp = [[0]*(length + 1) for _ in range(length+1)]

        prefix = stones[:]
        for i in range(1, length+1):
            prefix[i] += prefix[i-1]

        for l in range(2, length+1):
            for i in range(1, length-l+2):
                j = i + l - 1
                dp[i][j] = max(prefix[j] - prefix[i] - dp[i+1][j], prefix[j-1]- prefix[i-1] - dp[i][j-1])
        return dp[1][length]


