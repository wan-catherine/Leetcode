import collections
import math


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        ct = collections.Counter(s)
        if k > len(ct):
            return 0
        mapping = collections.defaultdict(int)
        for _, t in ct.items():
            mapping[t] += 1
        keys = sorted(mapping.keys(), reverse=True)
        k = min(k, 26)
        res = 1
        for i, key in enumerate(keys):
            if mapping[key] <= k:
                res *= key ** mapping[key]
                k -= mapping[key]
            else:
                res *= key ** k
                res *= math.perm(mapping[key], k) // math.perm(k, k)
                break
        return res % MOD

