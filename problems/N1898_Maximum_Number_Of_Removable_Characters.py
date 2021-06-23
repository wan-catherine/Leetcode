from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        lr, ls, lp = len(removable), len(s), len(p)
        def check(num):
            idx = set(removable[:num])
            j = 0
            for i, c in enumerate(s):
                if i in idx or p[j] != c:
                    continue
                j += 1
                if j == lp:
                    return True
            if j == lp:
                return True
            return False

        l, r = 0, lr + 1
        while l < r:
            mid = (r - l) // 2 + l
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1
