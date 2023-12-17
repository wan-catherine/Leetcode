import sys


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        length = len(s)
        def helper(start, end, d):
            count = 0
            for i in range(d):
                b, e = start + i, end - (d - i) + 1
                while b < e:
                    if s[b] != s[e]:
                        count += 1
                    b += d
                    e -= d
            return count

        ranges = [[sys.maxsize] * length for _ in range(length)]
        for i in range(length):
            for j in range(i, length):
                l = j - i + 1
                for d in range(1, l):
                    if l % d != 0:
                        continue
                    ranges[i][j] = min(ranges[i][j], helper(i, j, d))

        dp = [[sys.maxsize] * (k + 1) for _ in range(length)]
        for i in range(length):
            dp[i][1] = ranges[0][i]

        for i in range(length):
            for j in range(2, k + 1):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j-1] + ranges[p+1][i])

        return dp[length-1][k]



