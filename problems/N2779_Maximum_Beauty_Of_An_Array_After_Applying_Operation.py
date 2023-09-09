from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        arr = []
        for n in nums:
            arr.append((max(0, n - k), min(10**5,n + k )))
        arr.sort()
        count = [0] * (10**5 + 2)
        for s, e in arr:
            count[s] += 1
            count[e+1] -= 1
        res = 1
        current = 0
        for i in range(10**5 + 2):
            current += count[i]
            res = max(res, current)
        return res

