import collections
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        maximum = max(nums)
        arr = [-1]
        for i, n in enumerate(nums):
            if n == maximum:
                arr.append(i)
        if k > len(arr) - 1:
            return 0
        arr.append(length)
        array = []
        prefix = [0]

        for i in range(1, len(arr)):
            array.append(arr[i] - arr[i-1])
            prefix.append(prefix[-1] + array[-1])

        ans = 0
        for c in range(len(array) - k):
            ans += array[c] * (prefix[-1] - prefix[c + k])
        return ans

