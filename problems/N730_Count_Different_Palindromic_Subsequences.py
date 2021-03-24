class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        MOD = 10**9 + 7
        length = len(S)
        next, before = [[length]*4 for _ in range(length)] , [[-1]*4 for _ in range(length)]
        for i in range(length):
            flag = 0
            for j in range(i, length):
                if next[i][ord(S[j]) - ord('a')] == length:
                    next[i][ord(S[j]) - ord('a')] = j
                    flag += 1
                    if flag == 4:
                        break

        for i in range(length-1, -1, -1):
            flag = 0
            for j in range(i, -1, -1):
                if before[i][ord(S[j]) - ord('a')] == -1:
                    before[i][ord(S[j]) - ord('a')] = j
                    flag += 1
                    if flag == 4:
                        break
        # print(next)
        # print(before)
        dp = [[0]*length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1

        for l in range(2, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1
                for k in range(4):
                    p, q = next[i][k], before[j][k]
                    if p < q:
                        dp[i][j] += dp[p+1][q-1] + 1
                    if p <= j:
                        dp[i][j] += 1
                # print(i, j, dp[i][j])
        return dp[0][-1] % MOD

