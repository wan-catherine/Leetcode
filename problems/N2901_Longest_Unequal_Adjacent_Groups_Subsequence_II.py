from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        dp = [1] * n
        def check(a, c):
            if len(a) != len(c):
                return False
            diff = 0
            for i, w in enumerate(a):
                if w != c[i]:
                    diff += 1
            return diff == 1

        for i in range(1, n):
            for j in range(i):
                if groups[i] == groups[j]:
                    continue
                if not check(words[i], words[j]):
                    continue
                dp[i] = max(dp[i], dp[j] + 1)

        large = 0
        idx = 0
        for i in range(n):
            if dp[i] > large:
                large = dp[i]
                idx = i

        res = [words[idx]]
        prev = idx
        for i in range(idx -1, -1, -1):
            if groups[i] == groups[prev]:
                continue
            if not check(words[i], words[prev]):
                continue
            if dp[i] != dp[prev] - 1:
                continue
            res.append(words[i])
            prev = i
        return res[::-1]
