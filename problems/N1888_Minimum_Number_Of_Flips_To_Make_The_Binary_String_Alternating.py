"""
Key point :
    the rotate operation only helps when the first char of the first part is different from the second part's last char.
    and at the same time, the first and second parts are already alternating!
"""
class Solution:
    def minFlips(self, s: str) -> int:
        length = len(s)
        left10, left01 = [0] * length, [0] * length
        l10, l01 = 0, 0
        for i in range(length):
            if (i % 2 and s[i] == '1') or (not i % 2 and s[i] == '0'):
                l10 += 1
            if (i % 2 and s[i] == '0') or (not i % 2 and s[i] == '1'):
                l01 += 1
            left10[i] = l10
            left01[i] = l01
        right10, right01 = [0] * length, [0] * length
        r10, r01 = 0, 0
        for i in range(length-1, -1, -1):
            j = length - i - 1
            if (j % 2 and s[i] == '0') or (not j % 2 and s[i] == '1'):
                r10 += 1
            if (j % 2 and s[i] == '1') or (not j % 2 and s[i] == '0'):
                r01 += 1
            right10[i] = r10
            right01[i] = r01
        res = min(left01[-1], left10[-1])
        for i in range(length-1):
            res = min(res, left01[i] + right01[i+1], left10[i] + right10[i+1])
        return res

