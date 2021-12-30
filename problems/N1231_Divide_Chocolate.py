from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        length = len(sweetness)
        total = sum(sweetness)
        if k == 0:
            return total
        def check(val):
            count, cur = 0, 0
            for i in range(length):
                cur += sweetness[i]
                if cur >= val:
                    count += 1
                    cur = 0
            return count >= k + 1

        l, r = 1, total
        while l < r:
            mid = (r - l + 1) // 2 + l
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

