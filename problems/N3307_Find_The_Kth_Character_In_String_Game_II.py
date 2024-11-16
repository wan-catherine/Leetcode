import string
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cur = 1
        time = 0
        while cur < k:
            cur *= 2
            time += 1
        shift = 0
        for i in range(time-1, -1, -1):
            if k > cur // 2 :
                k = k - cur // 2
                if operations[i] == 1:
                    shift += 1
            cur //= 2
        return string.ascii_lowercase[shift % 26]
