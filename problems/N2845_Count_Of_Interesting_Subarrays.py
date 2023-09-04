import collections
from typing import List


class Solution:
    def countInterestingSubarrays_TLE(self, nums: List[int], modulo: int, k: int) -> int:
        arr = []
        for i, n in enumerate(nums):
            if n % modulo == k:
                arr.append(i)
        length = len(arr)

        def helper(n):
            if n == 0:
                res = 0
                if not arr:
                    return (len(nums) + 1) * len(nums) // 2
                prev = -1
                for i in arr:
                    res += (i - prev - 1) * (i - prev) // 2
                    prev = i
                res += (len(nums) - arr[-1] - 1) * (len(nums) - arr[-1]) // 2
                return res

            cur = 0
            prev = -1
            for i in range(n-1, length):
                if i < length - 1:
                    cur += (arr[i - n + 1] - prev) * (arr[i+1] - arr[i])
                else:
                    cur += (arr[i - n + 1] - prev) * (len(nums) - arr[i])
                prev = arr[i - n + 1]
            return cur

        a = 0
        res = 0
        while a * modulo + k <= length:
            res += helper(a * modulo + k)
            a += 1
        return res

    # hash prefix
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        mapping = collections.defaultdict(int)
        mapping[0] = 1
        length = len(nums)
        count = [0] * (length + 1)
        res = 0
        for i, n in enumerate(nums):
            count[i + 1] = count[i]
            if n % modulo == k:
                count[i + 1] += 1
            d = count[i + 1] % modulo
            res += mapping[(d - k + modulo) % modulo]
            mapping[d] += 1
        return res
