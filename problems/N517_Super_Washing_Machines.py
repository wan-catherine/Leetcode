from typing import List
"""
left[i] : the number of dress for i index get from left
right[i]: the number of dress for i index get from right

left[i] and right[i] can be positive and negative. 
positive : get dress, negative : give dress

left[i] + right[i] = machines[i] - val (in order to get val, it much get/throw left[i] + right[i] dresses)
left[i+1] = - right[i]

then we can find the largest give times (not max(left[i] + right[i]), because one of them might be negative. 
We only need to the largest GIVE times. 
"""

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        length, total = len(machines), sum(machines)
        if total % length:
            return -1
        val = total // length
        left, right = [0] * length, [0] * length
        right[0] = machines[0] - val
        left[length-1] = machines[length-1] -val
        for i in range(1, length - 1):
            left[i] = -right[i-1]
            right[i] = machines[i] - val - left[i]
        res = 0
        for i in range(length):
            cur = 0
            if left[i] > 0:
                cur += left[i]
            if right[i] > 0:
                cur += right[i]
            res = max(res, cur)
        return res
