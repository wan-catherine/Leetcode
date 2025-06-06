import collections


class Solution:
    def robotWithString(self, s: str) -> str:
        length = len(s)
        mapping = collections.defaultdict(list)
        for i, c in enumerate(s):
            mapping[c].append(i)

        res = ""
        cur = 0
        ans = []
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in mapping:
                continue
            index = mapping[ch][-1]
            if index >= cur:
                while ans and s[ans[-1]] <= ch:
                    res += s[ans.pop()]
                while cur <= index and cur < length:
                    if s[cur] != ch:
                        ans.append(cur)
                    else:
                        res += ch
                    cur += 1
            while ans and s[ans[-1]] < ch:
                res += s[ans.pop()]
        for i in ans[::-1]:
            res += s[i]
        return res