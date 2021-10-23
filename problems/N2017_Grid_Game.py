import sys
from typing import List

"""
the second robot only have two options : 
    right-top or left-down. 
    xxxx yyy
    zz xxxxx
       i
    
if the first robot goes down at index i, then the second robot can only get 'yyy' or 'zz'.

Key point: 
to make first robot get the maximum doesn't mean the second robot will get the minimum. 
"""

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        up, down = grid[0][:], grid[1][:]
        for i in range(length-2, -1, -1):
            up[i] += up[i+1]
        for i in range(1, length):
            down[i] += down[i-1]
        res = 0
        if length > 1:
            res = min(down[length-2], up[1])
        for i in range(1, length - 1):
            res = min(res, max(down[i-1], up[i+1]))
        return res
