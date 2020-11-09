import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        count = collections.Counter(arr)
        res = 0
        keys = sorted(count.keys(), reverse=True)
        for key in keys:
            if not key or count[key] <= 1:
                continue
            while count[key] > 1:
                n = key - 1
                while n != 0 and n in count:
                    n -= 1
                res += key - n
                count[n] += 1
                count[key] -= 1
        return res