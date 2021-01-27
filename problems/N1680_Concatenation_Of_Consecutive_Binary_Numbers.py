"""
from '110' --> '11000':
 110 * (1 << 2)
"""
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:
            return 1
        mod = 10 ** 9 + 7
        cur = 2
        ans = 1
        i = 2
        while cur <= n:
            ans *= 1 << i
            ans += cur
            ans %= mod
            cur += 1
            if cur >= 2 ** i:
                i += 1
        return ans