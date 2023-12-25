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
    def numberOfSequence_(self, n: int, sick: List[int]) -> int:
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