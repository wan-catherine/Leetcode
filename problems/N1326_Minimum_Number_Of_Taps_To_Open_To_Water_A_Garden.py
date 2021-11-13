from typing import List

"""
Convert it into intervals problem. 
It's similar as LC 1024
"""

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(n+1):
            intervals.append([i-ranges[i], i+ranges[i]])
        intervals.sort(key=lambda x :(x[0], -x[1]))
        res = 0
        e = 0
        i = 0
        while i <= n:
            ne = e
            while i <= n and intervals[i][0] <= e:
                ne = max(ne, intervals[i][1])
                i += 1
            res += 1
            if ne >= n:
                return res
            if ne == e:
                return -1
            e = ne

        return -1



