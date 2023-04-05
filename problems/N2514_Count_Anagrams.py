import collections
import math


class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split(' ')
        res = 1
        for word in words:
            cw = collections.Counter(word)
            l = len(word)
            res *= math.perm(l)
            for k, v in cw.items():
                res //= math.perm(v)
        return res % (10**9 + 7)
