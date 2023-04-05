import math
import sys


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r = 1, sys.maxsize
        def lcm(a, b):
            return a * b // math.gcd(a, b)

        def check(m):
            a, b = m - m // divisor1, m - m // divisor2
            c = m - (m // divisor1 + m // divisor2 - m // lcm(divisor1, divisor2))
            if a < uniqueCnt1 or b < uniqueCnt2 or a + b - c < uniqueCnt1 + uniqueCnt2:
                return True
            return False

        while l < r:
            mid = (r - l) // 2 + l
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l

