from typing import List


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def check(num):
            for i in range(k):
                cur = 0
                for j in range(n):
                    cur += (max(0, composition[i][j] * num - stock[j])) * cost[j]
                if cur <= budget:
                    return True
            return False

        l, r = 0, 10**9
        while l < r:
            mid = (r + l + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

