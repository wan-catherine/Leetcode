from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        ln, lq = len(nums), len(queries)
        def check(idx):
            arr = [0] * (ln + 1)
            for l, r, v in queries[:idx]:
                arr[l] += v
                arr[r + 1] -= v
            cur = 0
            for i in range(ln):
                cur += arr[i]
                if nums[i] > cur:
                    return False
            return True

        if not check(lq):
            return -1

        l, r = 0, lq
        while l < r:
            m = (r - l) // 2 + l
            if check(m):
                r = m
            else:
                l = m + 1
        return l
