import math
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs_TLE(self, nums: List[int]) -> int:
        memo = {}
        def gcd(a, b):
            a, b = max(a, b), min(a, b)
            while b:
                a, b = b, a % b
            memo[(a, b)] = a
            return a

        nums = set(nums)
        mapping = [0] * (2* 10 **5 + 1)
        for num in nums:
            for val in range(1, int(math.sqrt(num)) + 1):
                if num % val == 0:
                    if mapping[val] == 0:
                        mapping[val] = num
                    else:
                        if (mapping[val], num) in memo:
                            mapping[val] = memo[(mapping[val], num)]
                        else:
                            mapping[val] = gcd(mapping[val], num)
                    v = num // val
                    if mapping[v] == 0:
                        mapping[v] = num
                    else:
                        if (mapping[v], num) in memo:
                            mapping[v] = memo[(mapping[v], num)]
                        else:
                            mapping[v] = gcd(mapping[v], num)
        ans = 0
        for index in range(1, 2* 10 **5 + 1):
            if index == mapping[index]:
                ans += 1
        return ans

    """
    Think about gcd, then check if it can be get by using subsequence from nums
    """
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        maximum = max(nums)
        for n in range(1, maximum + 1):
            g = 0
            for nn in range(n, maximum + 1, n):
                if nn in nums:
                    g = math.gcd(g, nn)
            if g == n:
                ans += 1
        return ans