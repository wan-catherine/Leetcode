import sys
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for i in range(right + 1)]
        p = 2
        while p * p <= right:
            if prime[p]:
                for i in range(p * p, right + 1, p):
                    prime[i] = False
            p += 1
        res = [-1, -1]
        cur = -1
        for i in range(max(2, left), right + 1):
            if prime[i]:
                cur = i
                break
        if cur == -1:
            return res
        diff = sys.maxsize
        for i in range(cur + 1, right + 1):
            if not prime[i]:
                continue
            if i - cur < diff:
                res = [cur, i]
                diff = i - cur
            cur = i
        return res
