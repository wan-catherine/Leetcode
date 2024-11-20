import collections


class Solution:
    def takeCharacters_old(self, s: str, k: int) -> int:
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

    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        length = len(s)
        ct = collections.Counter(s)

        def check(ct):
            if 'a' not in ct or ct['a'] < k:
                return False
            if 'b' not in ct or ct['b'] < k:
                return False
            if 'c' not in ct or ct['c'] < k:
                return False
            return True

        if not check(ct):
            return -1
        s += s
        res = length
        cur = collections.Counter()
        j = 0
        for i in range(length):
            while j < 2 * length and not check(cur):
                cur[s[j]] += 1
                j += 1
            if j == 2 * length:
                break
            if i == 0 or j > length - 1:
                res = min(res, j - i)
            else:
                res = min(res, length - i)
            cur[s[i]] -= 1
        return res