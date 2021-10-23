import collections
from typing import List

"""
xxxxx i xxxxx  
when change i to k , the prefix[i-1] and suffix[i+1] never change.
So we can directly use it . 
"""

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        length, total = len(nums), sum(nums)
        prefix, suffix = nums[:], nums[:]
        for i in range(1, length):
            prefix[i] += prefix[i-1]
        for i in range(length-2, -1, -1):
            suffix[i] += suffix[i+1]
        pre = collections.defaultdict(int)
        res = [0] * length
        for i in range(length):
            new_total = total - nums[i] + k
            if i > 0 and new_total % 2 == 0:
                res[i] += pre[new_total//2]
            pre[prefix[i]] += 1
        suf = collections.defaultdict(int)
        for i in range(length-1, -1, -1):
            new_total = total - nums[i] + k
            if i < length - 1 and new_total % 2 == 0:
                res[i] += suf[new_total//2]
            suf[suffix[i]] += 1
        ans = 0
        for i in range(length):
            if i < length -1 and prefix[i] == total // 2:
                ans += 1
        return max(max(res), ans)

