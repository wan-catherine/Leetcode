import sys
from typing import List

"""
knapsack problem. 
Constraints:
        m == mat.length
        n == mat[i].length
        1 <= m, n <= 70
        1 <= mat[i][j] <= 70  ==> capacity will be 70 * 70 
        1 <= target <= 800

If we directly use brute force, the time complexity will be 70**70. 
But if we consider capacity of a knapsack , it will be 70 * 70 * capacity. 
But 70**4 will also be TLE. 

It says : 1 <= target <= 800, so we can just keep the minimum number which > target . 
"""
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        dp = set()
        dp.add(0)
        for i in range(m):
            gt = sys.maxsize
            dp_new = set()
            for num in dp:
                for j in range(n):
                    val = mat[i][j] + num
                    if val <= target:
                        dp_new.add(val)
                    elif val < gt:
                        gt = val
            if gt < sys.maxsize:
                dp_new.add(gt)
            dp = dp_new
        diff = sys.maxsize
        for n in dp:
            if abs(n - target) < diff:
                diff = abs(n - target)
        return diff
