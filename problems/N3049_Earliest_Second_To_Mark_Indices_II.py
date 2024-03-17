import heapq
from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        nums = [0] + nums
        changeIndices = [0] + changeIndices
        n, m = len(nums), len(changeIndices)
        total = sum(nums)

        def check(t):
            if t < n - 1:
                return False
            first = [0] * n
            for i in range(1, t+1):
                if first[changeIndices[i]] == 0 and nums[changeIndices[i]] != 0:
                    first[changeIndices[i]] = i
                else:
                    changeIndices[i] = 0
            pq = []
            for i in range(t, 0, -1):
                idx = changeIndices[i]
                if idx == 0:
                    continue
                heapq.heappush(pq, nums[idx])
                marks = t - i + 1 - len(pq)
                if len(pq) > marks:
                    heapq.heappop(pq)
            acc = sum(pq)
            return acc + (t - n - len(pq) + 1) >= total

        l, r = 1, m
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l if l>0 and l < m else -1
