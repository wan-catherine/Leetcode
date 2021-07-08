import sys
from typing import List

"""
Dp problem:
There are two situation: 
1. a, b in the two side of half-point
2. a, b in the left side of half-point
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1900.The-Earliest-and-Latest-Rounds-Where-Players-Compete

"""
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        de, dl = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)], [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
        def helper(l, a, b):
            if de[l][a][b] != 0:
                return (de[l][a][b], dl[l][a][b])
            if a + b == l + 1:
                return [1, 1]
            if a > b:
                return helper(l, b, a)
            if a + b > l + 1:
                return helper(l, l + 1 - b, l + 1 - a)
            half_point = (l + 1) // 2
            maxv, minv = 0, sys.maxsize
            range1, bb = a - 1, l + 1 - b
            if b > half_point:
                range2 = bb - a - 1
                mid = b - bb - 1
                for x in range(range1 + 1):
                    for y in range(range2 + 1):
                        temp = helper((l+1)//2, x + 1, x + 1 + y + (mid + 1) // 2 + 1)
                        maxv = max(maxv, temp[1] + 1)
                        minv = min(minv, temp[0] + 1)
            else:
                range2 = b - a - 1
                for x in range(range1 + 1):
                    for y in range(range2 + 1):
                        temp = helper((l+1)//2, x + 1, x + 1 + y + 1)
                        maxv = max(maxv, temp[1] + 1)
                        minv = min(minv, temp[0] + 1)
            de[n][a][b] = minv
            dl[n][a][b] = maxv
            return [minv, maxv]

        return helper(n, firstPlayer, secondPlayer)
