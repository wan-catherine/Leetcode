"""
num = a^k1*b^k2*c^k3*...
primeFactors = k1+k2+k3+...
nice_divisor = k1*k2*k3...

There is a conclusion : we split those numbers as 3 and 2, then the mulitple is the maximum.
let 3 as many as possible.

https://github.com/wisdompeak/LeetCode/tree/master/Math/1808.Maximize-Number-of-Nice-Divisors
"""
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        """
        we need this function , if we directly use : 3**a, it will be TLE.
        """
        def quick_mul(x, n):
            if not n:
                return 1
            y = quick_mul(x, n//2)
            if n % 2 == 0:
                return y * y % MOD
            else:
                return y * y * x % MOD

        if primeFactors <= 4:
            return primeFactors

        if primeFactors % 3 == 0:
            a, b = primeFactors//3, 0
        elif primeFactors % 3 == 2:
            a, b = (primeFactors - 2)//3, 1
        else:
            a, b = (primeFactors - 4)//3, 2

        MOD = 10**9 + 7
        res = quick_mul(3, a) % MOD
        res *= quick_mul(2, b) % MOD
        return res