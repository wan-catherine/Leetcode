import sys


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        def check(base, count):
            return (base ** count - 1) // (base - 1)
        ans = sys.maxsize
        for i in range(1, 64):
            l, r = 2, num
            while l < r:
                m = (r - l) // 2 + l
                val = check(m, i)
                if val == num:
                    ans = min(ans, m)
                    break
                if val < num:
                    l = m + 1
                else:
                    r = m
        return str(ans)