import sys


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        left, right = [sys.maxsize] * lt, [-1] * lt
        j = 0
        for i in range(lt):
            while j < ls and s[j] != t[i]:
                j += 1
            if j < ls:
                left[i] = j
                j += 1
        j = ls - 1
        for i in range(lt-1, -1, -1):
            while j >= 0 and s[j] != t[i]:
                j -= 1
            if j >= 0:
                right[i] = j
                j -= 1

        def check(m):
            if left[lt - m - 1] != sys.maxsize:
                return True
            if right[m] != -1:
                return True
            for i in range(1, lt - m):
                if left[i - 1] < right[i + m]:
                    return True
            return False

        l, r = 0, lt
        while l < r:
            mid = (r - l) // 2 + l
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l