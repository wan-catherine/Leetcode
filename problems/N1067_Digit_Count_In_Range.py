"""
we need to seperate d == 0 and d > 0 . 
"""
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def helper_zero(number):
            snumber = str(number)
            length = len(snumber)
            ans = 0
            for i in range(1, length):
                v = int(snumber[i])
                if v > 0:
                    left = int(snumber[:i])
                    right = 10 ** (length - i - 1)
                    ans += left * right
                else:
                    left = int(snumber[:i]) - 1
                    right = 10 ** (length - i - 1)
                    ans += left * right
                    right = 1 + (int(snumber[i+1:]) if snumber[i+1:] else 0)
                    ans += right
            return ans

        def helper(number):
            nonlocal d
            snumber = str(number)
            length = len(snumber)
            ans = 0
            for i in range(length):
                v = int(snumber[i])
                if v > d:
                    left = (int(snumber[:i]) if snumber[:i] else 0) + 1
                    right = 10 ** (length - i - 1)
                    ans += left * right
                elif v < d:
                    left = int(snumber[:i]) if snumber[:i] else 0
                    right = 10 ** (length - i - 1)
                    ans += left * right
                else:
                    left = int(snumber[:i]) if snumber[:i] else 0
                    right = 10 ** (length - i - 1)
                    ans += left * right
                    left = 1
                    right = (int(snumber[i+1:]) if snumber[i+1:] else 0) + 1
                    ans += left * right
            return ans

        if d > 0:
            return helper(high) - helper(low-1)
        else:
            return helper_zero(high) - helper_zero(low - 1)
