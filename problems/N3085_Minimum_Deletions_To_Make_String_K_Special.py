import collections


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        ct = sorted(collections.Counter(word).values())
        length = len(ct)
        res = len(word)
        pre = 0
        for i in range(length):
            ans = 0
            for j in range(i + 1, length):
                if ct[j] - ct[i] > k:
                    ans += ct[j] - ct[i] - k
            res = min(res, ans + pre)
            pre += ct[i]
        return res