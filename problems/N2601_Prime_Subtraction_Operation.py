import bisect
from typing import List
from others.Primes import Primes

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = Primes().get_primes(1000)
        # print(primes)
        length = len(primes)
        prev = 0
        for i, n in enumerate(nums):
            if n < i + 1:
                return False
            if n <= prev:
                return False
            idx = bisect.bisect_left(primes, n - prev)
            if idx == 0:
                if primes[idx] == n - prev:
                    return False
                if primes[idx] > n - prev:
                    prev = n
                    continue
            if idx == length or primes[idx] >= n - prev:
                idx -= 1
            prev = n - primes[idx]
            print(prev)
        return True
