import math
from typing import List

"""
Key point is : All the mechanics can repair the cars simultaneously.
So for some times, we can calculate the cars all mechanics together can repair. 
If the number of cars >= given cars , then we reduce the times, or we increase the times. 
So perfect binary search .
"""
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, 100 * 10 ** 6 * 10 ** 6 + 1
        def check(mid):
            cur = 0
            for r in ranks:
                cur += int(math.sqrt(mid / r))
            if cur >= cars:
                return True
            return False

        while l < r:
            mid = (r - l) // 2 + l
            # print(r, l, mid)
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


