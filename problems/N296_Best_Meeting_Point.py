"""
Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
Find a point(x, y) ==>
|p1.x - x| + |p1.y - y| + |p2.x - x| + |p2.y - y| + .. + |pn.x - x| + |pn.y - y| ==>
(|p1.x - x| + |p2.x - x| + .. + |pn.x - x|)  + (|p1.y - y| + |p2.y - y| + .. + |pn.y - y|)
==> so we can get the x, y separately which is in one dimension.
x, y are the medium of the array.

extension:
1. what if the distance has some weight ?
    then find the weight medium . w1, w2, w3 , ..., wn . find the p which [0,p-1] + p > [p+1,n], [0,p-1] < p+[p+1,n]
"""
from typing import List


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xarr, yarr = [], []
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    xarr.append(j)
                    yarr.append(i)
        xarr.sort()
        yarr.sort()
        x, y = xarr[len(xarr)//2], yarr[len(yarr)//2]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    res += abs(j - x)
                    res += abs(i - y)
        return res

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        xarr, yarr = [], []
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    xarr.append(j)
                    yarr.append(i)
        xarr.sort()
        yarr.sort()
        x = xarr[len(xarr) // 2]
        y = yarr[len(yarr) // 2]
        res = 0
        for i in range(len(xarr)):
            res += abs(xarr[i] - x)
        for i in range(len(yarr)):
            res += abs(yarr[i] - y)
        return res