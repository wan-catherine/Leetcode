"""
dp[i][j] : a list of length j ( there are j different number which increased sort), the last number is i.

    dp[i*2][j+1] += dp[i][j]
    dp[i*3][j+1] += dp[i][j]
    ....
    dp[i*x][j+1] += dp[i][j] (i*x <= maxValue)

dp[i][j], there is no duplicated number , but this problem we need to duplicated the number from j to n .
This is a classical method for this kind of problem : 隔板法

we have n numbers , so we have n - 1 space to insert . Now we need to insert j - 1 , then the whole n numbers split by j
cluster , each cluster is a list of same number .

for dp[i][j], there are j numbers , we need to duplicated them to n numbers .
so there are combination math problem .

"""
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 15 for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            dp[i][1] = 1
        for j in range(1, 14):
            for i in range(1, maxValue + 1):
                k = 2
                while k * i <= maxValue:
                    dp[k * i][j + 1] += dp[i][j]
                    dp[k * i][j + 1] %= MOD
                    k += 1
        combination = [[0] * 15 for _ in range(n)]
        for i in range(n):
            for j in range(min(14, i) + 1):
                if j == 0:
                    combination[i][j] = 1
                else:
                    combination[i][j] = (combination[i-1][j] + combination[i-1][j-1]) % MOD
        res = 0
        for i in range(1, maxValue + 1):
            for j in range(1, min(14, n) + 1):
                res = (res + dp[i][j] * combination[n-1][j-1]) % MOD
        return res
