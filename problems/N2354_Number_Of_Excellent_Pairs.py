import bisect
import collections
from typing import List


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        snums = set(nums)
        res = 0
        arr = []
        for i, n in enumerate(snums):
            count = 0
            while n:
                if n & 1:
                    count += 1
                n >>= 1
            bisect.insort_left(arr, count)
            if count * 2 >= k:
                res += 1
        length = len(arr)
        # r = length
        # for i in range(length):
        #     while r > 0 and arr[i] + arr[r - 1] >= k:
        #         r -= 1
        #     res += length - r
        # return res
        l, r = 0, length - 1
        while l < length:
            while r >= 0 and arr[l] + arr[r] >= k:
                r -= 1
            res += length - 1 - r
            l += 1
        return res
    """
    There is a great idea to avoid duplication . 
    Here we have n different number : xxxxxx 
    then we pick up two of them : n * (n - 1) 
    if all n number still satisfied some condition (here is i + j >= k), then have n more . 
    n * (n - 1) + n = n * n 
    """
    def countExcellentPairs_great(self, nums: List[int], k: int) -> int:
        snums = set(nums)
        res = 0
        counter = collections.Counter()
        for i, n in enumerate(snums):
            count = 0
            while n:
                if n & 1:
                    count += 1
                n >>= 1
            counter[count] += 1
        for i in range(0, 31):
            for j in range(0, 31):
                if i + j >= k:
                    res += counter[i] * counter[j]
        return res

    def countExcellentPairs_20250214(self, nums: List[int], k: int) -> int:
        ct = collections.Counter(nums)
        nums = ct.keys()
        arr = []
        length = len(nums)
        for n in nums:
            bisect.insort_left(arr, bin(n).count('1'))
        res = 0
        j = length - 1
        for i in range(length):
            while j >=0 and arr[i] + arr[j] >= k:
                j -= 1

            if j < i:
                res += 1 + (length - i - 1) * 2
            elif j == i:
                res += (length - i - 1) * 2
            else:
                res += (length - j - 1) * 2
        return res
