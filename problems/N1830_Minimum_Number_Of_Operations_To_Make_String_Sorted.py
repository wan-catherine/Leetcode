"""
(a * b) % mod = a % mod * b % mod
(a / b) % mode = a % mode * inv(b)
inv(b) : b's inverse element
"""
class Solution:
    def makeStringSorted(self, s: str) -> int:
        frequency = [0] * 26
        mod = 10**9 + 7
        for c in s:
            frequency[ord(c) - ord('a')] += 1
        factorial = [0] * 3001
        factorial[0] = 1
        for i in range(1, 3001):
            factorial[i] = factorial[i-1] * i % mod

        def inv(num):
            s = 1
            while num > 1:
                s = s * (mod - mod // num) % mod
                num = mod % num
            return s

        res = 0
        length = len(s)
        for i in range(length):
            count = sum(frequency[:ord(s[i]) - ord('a')])
            ans = count * factorial[length - i - 1] % mod
            for k in range(26):
                # remove the permutation of duplicated number
                # res = (res // factorial[frequency[k]]) % mod
                ans = ans * inv(factorial[frequency[k]]) % mod
            res = (res + ans) % mod
            frequency[ord(s[i]) - ord('a')] -= 1
        return res
