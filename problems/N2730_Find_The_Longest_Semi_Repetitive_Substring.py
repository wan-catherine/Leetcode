class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 2:
            return length
        res = 2
        cur = 0
        j = 0
        for i in range(length - 1):
            while j < length - 1 and cur < 2:
                if s[j] == s[j + 1]:
                    cur += 1
                j += 1
            if cur == 2:
                res = max(res, j - i)
            else:
                res = max(res, j - i + 1)
            if cur == 2:
                if s[i] == s[i+1]:
                    cur -= 1
                continue
        return res
