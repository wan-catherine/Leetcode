from typing import List

"zero-sum"
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        arr = [0] * 32
        MOD = 10 ** 9 + 7
        for n in nums:
            for i in range(32):
                if n & (1 << i):
                    arr[i] += 1
        res = 0
        for _ in range(k):
            cur = 0
            for i in range(32):
                if arr[i] > 0:
                    cur += (1 << i)
                    arr[i] -= 1
            res += cur ** 2
            res %= MOD
        return res

