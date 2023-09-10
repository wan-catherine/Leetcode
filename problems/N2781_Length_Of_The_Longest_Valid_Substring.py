from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        fset = set(forbidden)
        length = len(word)
        def check(st):
            lst = len(st)
            l = min(10, lst)
            for i in range(1, l + 1):
                if st[lst - i:] in fset:
                    return False
            return True

        l, r = 0, 0
        res = 0
        for i in range(length):
            while not check(word[l:r+1]):
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

