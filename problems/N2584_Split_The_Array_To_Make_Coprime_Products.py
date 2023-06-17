import collections
from typing import List
from others.Primes import *

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        primes = Primes().get_primes(max(nums) + 1)
        length = len(nums)

        # TLE
        # intervels = []
        # for p in primes:
        #     f, s = -1, -1
        #     for i, n in enumerate(nums):
        #         if n % p == 0:
        #             f = i
        #             break
        #     if f == -1:
        #         continue
        #     s = f
        #     for i in range(length - 1, -1, -1):
        #         if nums[i] % p == 0:
        #             s = i
        #             break
        #     intervels.append([f, s])

        map = collections.defaultdict(list)
        for i, n in enumerate(nums):
            x = n
            for p in primes:
                if x == 1:
                    break
                if p * p > x:
                    if x not in map:
                        map[x].extend([i, i])
                    map[x][1] = i
                    break
                if x % p == 0:
                    if p not in map:
                        map[p].extend([i, i])
                    map[p][1] = i
                while x % p == 0:
                    x //= p

        intervels = []
        for k, li in map.items():
            intervels.append(li)


        diff = [0] * (length + 1)
        for u, v in intervels:
            diff[u] += 1
            diff[v] -= 1

        cur = 0
        for i in range(length - 1):
            cur += diff[i]
            if cur == 0:
                return i
        return -1

