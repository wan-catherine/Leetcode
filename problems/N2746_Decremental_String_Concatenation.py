import collections
import string
import sys
from typing import List


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        length = len(words)
        dp = [[[sys.maxsize] * 26 for _ in range(26)] for _ in range(length)]
        dp[0][ord(words[0][0]) - ord('a')][ord(words[0][-1]) - ord('a')] = len(words[0])
        for i in range(1, length):
            s, e = ord(words[i][0]) - ord('a'), ord(words[i][-1]) - ord('a')
            for p in range(26):
                for q in range(26):
                    if dp[i-1][p][q] < sys.maxsize:
                        dp[i][p][e] = min(dp[i][p][e], dp[i-1][p][q] + len(words[i]))
                        dp[i][s][q] = min(dp[i][s][q], dp[i-1][p][q] + len(words[i]))
            for c in range(26):
                if dp[i-1][c][s] < sys.maxsize:
                    dp[i][c][e] = min(dp[i][c][e], dp[i-1][c][s] + len(words[i]) - 1)
                if dp[i-1][e][c] < sys.maxsize:
                    dp[i][s][c] = min(dp[i][s][c], dp[i-1][e][c] + len(words[i]) - 1)

        res = sys.maxsize
        for s in range(26):
            for e in range(26):
                res = min(res, dp[-1][s][e])
        return res

