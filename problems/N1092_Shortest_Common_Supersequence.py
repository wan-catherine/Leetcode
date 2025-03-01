class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        first = '#' + str1
        second = '#' + str2
        lf, ls = len(first), len(second)
        dp = [[0] * ls for _ in range(lf)]
        for i in range(lf):
            dp[i][0] = i
        for j in range(ls):
            dp[0][j] = j
        for i in range(1, lf):
            for j in range(1, ls):
                if first[i] == second[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        res = []
        i, j = lf-1, ls-1
        while i > 0 and j > 0:
            if first[i] == second[j]:
                res.append(first[i])
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i-1][j] + 1:
                res.append(first[i])
                i -= 1
            else:
                res.append(second[j])
                j -= 1
        while i > 0:
            res.append(first[i])
            i -= 1
        while j > 0:
            res.append(second[j])
            j -= 1
        return ''.join(res[::-1])

