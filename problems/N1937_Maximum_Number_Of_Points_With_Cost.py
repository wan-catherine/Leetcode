from typing import List

"""
For current row, it depends on previous row result and its column index. 
Here is a great explanation : https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/Python-3-DP-Explanation-with-pictures.
res[i] = max(pre[j] - abs(j-i) for j in range(n)) + points[i][j]

we can see the first part as cur[i] = max(pre[j] - abs(j-i) for j in range(n))

Then we consider left and right part . 
Left: 
    cur[i] = max(cur[i-1] - 1, pre[i])
Right:
    cur[i] = max(cur[i+1] - 1, cur[i])
    
Then:
    res[i] = cur[i] + points[row][i]
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev, cur = points[0], [0] * n

        for i in range(1, m):
            cur[0] = prev[0]
            for j in range(1, n):
                cur[j] = max(prev[j], cur[j-1] - 1)
            for j in range(n-2, -1, -1):
                cur[j] = max(cur[j], cur[j+1] - 1)
            for j in range(n):
                prev[j] = cur[j] + points[i][j]
        return max(prev)
