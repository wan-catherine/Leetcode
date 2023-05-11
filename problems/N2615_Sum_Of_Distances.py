import collections
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)

        def helper(li):
            length = len(li)
            if length == 1:
                return
            pre, suf = [0] * length, [0] * length
            p = 0
            for i in range(length):
                p += li[i]
                pre[i] = p
            s = 0
            for i in range(length - 1, -1, -1):
                s += li[i]
                suf[i] = s
            for i, idx in enumerate(li):
                arr[idx] = (i + 1) * idx - pre[i] + suf[i] - (length - i) * idx

        status = collections.defaultdict(list)
        for i, n in enumerate(nums):
            status[n].append(i)

        for n, li in status.items():
            helper(li)
        return arr