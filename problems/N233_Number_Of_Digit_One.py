"""
xxxxxxx...xxxx
consider one by one:
xxxx..[i]..xxx
situation :
    1. i > 1
    2. i == 1
    3. i < 1 (i == 0)

Count ith digit == 1.
"""
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        sn = str(n)
        length = len(sn)
        ans = 0
        for i in range(length):
            v = int(sn[i])
            if v == 0:
                left = (int(sn[:i]) if sn[:i] else 0)
                right = 10 ** (length - i - 1)
                ans += left * right
            if v > 1:
                left = 1 + (int(sn[:i]) if sn[:i] else 0)
                right = 10 ** (length - i - 1)
                ans += left * right
            elif v == 1:
                left = int(sn[:i]) if sn[:i] else 0
                right = 10 ** (length - i - 1)
                ans += left * right
                left = 1
                right = 1 + (int(sn[i+1:]) if sn[i+1:] else 0)
                ans += left * right
        return ans


