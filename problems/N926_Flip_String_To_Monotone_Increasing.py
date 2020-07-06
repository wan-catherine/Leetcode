class Solution(object):
    def minFlipsMonoIncr_prefix_suffix(self, S):
        """
        :type S: str
        :rtype: int
        """
        length = len(S)
        zero = [0] * length
        zero[0] = 0 if S[0] == '0' else 1
        one = [0] * length
        one[-1] = 0 if S[-1] == '1' else 1
        for i in range(1, length):
            zero[i] = zero[i-1] + (1 if S[i] == '1' else 0)
            one[length-i-1] = one[length-i] + (1 if S[length-i-1] == '0' else 0)
        res = length
        for i in range(length-1):
            res = min(res, zero[i] + one[i+1])
        res = min(res, zero[length-1], one[0])
        return res

    """
    dp[i+1][0] : flip times when S[i] changes into zero
    dp[i+1][1] : flip time when S[i] changes into one
    
    dp[i+1][0] = dp[i][0] + (1 if S[i] == '1' else 0)
    dp[i+1][1] = min(dp[i][0], dp[i][1]) + (1 if S[i] == '0' else 0)
    """
    def minFlipsMonoIncr_dp(self, S):
        length = len(S)
        dp = [[0,0] for _ in range(length+1)]
        for i, v in enumerate(S):
            if v == '0':
                dp[i+1][0] = dp[i][0]
                dp[i+1][1] = min(dp[i][1], dp[i][0]) + 1
            else:
                dp[i+1][0] = dp[i][0] + 1
                dp[i+1][1] = min(dp[i][0], dp[i][1])
        return min(dp[-1][0], dp[-1][1])
