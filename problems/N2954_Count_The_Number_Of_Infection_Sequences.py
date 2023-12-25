from functools import cache
from itertools import pairwise
from typing import List

"""
ret = n!;
for (int i=0; i<k; i++)
  ret = ret / mi! * (2^mi);
  
(A*B)%M = (A%M) * (B%M), 
but for "/", 
inv(a) = a ^ (M-2) % M
"""

class Solution:
    def numberOfSequence_MLE(self, n: int, sick: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def fact(i: int) -> int:
            return 1 if i < 2 else i * fact(i - 1) % MOD

        @cache
        def ifact(i: int) -> int:
            return pow(fact(i), -1, MOD)

        res = fact(n - len(sick)) * ifact(sick[0]) * ifact(n - sick[-1] - 1) % MOD
        for group in [b - a - 1 for a, b in pairwise(sick) if b - a > 1]:
            res = res * ifact(group) % MOD
            res = res * pow(2, group - 1, MOD) % MOD
        return res

    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10 ** 9 + 7
        group = []
        length = len(sick)
        for i in range(length):
            if i == 0:
                group.append(sick[i])
            else:
                group.append(sick[i] - sick[i-1] - 1)
        group.append(n - sick[-1] - 1)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = i * fact[i-1]
        def quickPow(x, y):
            res, cur = 1, x
            while y > 0:
                if y & 1:
                    res = res * cur % MOD
                cur = cur * cur % MOD
                y >>= 1
            return res

        def inv(x):
            return quickPow(x, MOD - 2)

        res = fact[length]
        for g in group:
            res = res * inv(fact[g]) % MOD

        for i in range(1, length):
            x = sick[i] - sick[i-1] - 1
            if x > 0:
                res = res * pow(2, x, MOD) % MOD

        return res


