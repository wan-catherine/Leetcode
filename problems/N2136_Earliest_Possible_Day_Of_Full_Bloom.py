from typing import List
"""
At first, I thought need to pick the one which (plantTime + growTime) is the longest . 
But whatever the result is , we at least need sum(plantTime) to plant . 
So just need to consider the longest of growTime, to plant it first . 
"""

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        length = len(plantTime)
        res = 0
        pq = [(plantTime[i], growTime[i]) for i in range(length)]
        pq.sort(key=lambda x: (-x[1]))
        cur = 0
        for time, grow in pq:
            cur += time
            res = max(res, cur + grow)
        return res