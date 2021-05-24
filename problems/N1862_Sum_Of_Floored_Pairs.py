import collections
from typing import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        count = [0] * (10 ** 5 + 1)
        for n in nums:
            count[n] += 1
        prev = count[:]
        for i in range(1, 10 ** 5 + 1):
            prev[i] += prev[i - 1]
        ans = 0

        visited = set()
        for x in nums:
            if x in visited:
                continue
            k = 1
            res = 0
            while x * (k + 1) - 1 <= 10 ** 5:
                res += k * (prev[x * (k + 1) - 1] - prev[x * k - 1])
                k += 1
            if x * (k + 1) - 1 > 10 ** 5 >= x * k - 1:
                res += k * (prev[10 ** 5] - prev[x * k - 1])
            ans += res * count[x]
            visited.add(x)
        return ans % (10 ** 9 + 7)
