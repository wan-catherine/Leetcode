import collections


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        length = len(s)
        cs = collections.Counter(s)
        for c in 'abc':
            if cs[c] < k:
                return -1
        ss = s + s
        def check(ss):
            l, r = 0, 0
            ct = collections.defaultdict(int)
            res = length
            while r < length * 2:
                ct[ss[r]] += 1
                while ct['a'] >= k and ct['b'] >= k and ct['c'] >= k:
                    if (r >= length and l < length) or l == 0 or r == length - 1:
                        res = min(res, r - l + 1)
                    ct[ss[l]] -= 1
                    l += 1
                r += 1
            return res
        res = length
        res = min(res, check(ss))
        res = min(res, check(ss[::-1]))
        return res