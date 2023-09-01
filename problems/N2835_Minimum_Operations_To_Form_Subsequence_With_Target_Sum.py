import collections
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        arr = [0] * 32
        for n in nums:
            i = 0
            while 2 ** i < n:
                i += 1
            arr[i] += 1

        res = 0
        for i in range(32):
            if (target >> i) & 1 == 1:
                if arr[i] > 0:
                    arr[i] -= 1
                else:
                    j = i + 1
                    while j < 32 and arr[j] == 0:
                        j += 1
                    if j == 32:
                        return -1
                    arr[j] -= 1
                    for k in range(i, j):
                        arr[k] += 1
                    res += j - i
            if arr[i] > 1 and i < 31:
               arr[i+1] += arr[i] // 2
               arr[i] = arr[i] % 2
        return res


