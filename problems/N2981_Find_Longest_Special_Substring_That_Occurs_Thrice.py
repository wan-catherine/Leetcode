import collections


class Solution:
    def maximumLength(self, s: str) -> int:
        mapping = collections.defaultdict(list)
        ls = len(s)
        l, r = 0, 0
        count = 0
        while r < ls:
            while r < ls and s[r] == s[l]:
                count += 1
                r += 1
            mapping[s[l]].append(count)
            l = r
            count = 0
        res = -1
        # print(mapping)
        for k, d in mapping.items():
            if sum(d) < 3:
                continue
            d.sort(reverse=True)
            ld = len(d)
            if ld >= 1 and d[0] >= 3:
                res = max(res, d[0] - 2)
            if ld >= 2:
                res = max(res, min(d[0] - 1, d[1]))
            if ld >= 3:
                res = max(res, min(d[:3]))

        return res