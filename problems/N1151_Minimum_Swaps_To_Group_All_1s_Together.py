import collections
from typing import List

"""
we know how many 1 in total, so for any window which length is num of 1, 
we can calculate who many zeros in this window and get the minimum. 
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        length = len(data)
        counter = collections.Counter(data)
        if 1 not in counter or counter[1] == 1:
            return 0
        k = counter[1]
        res = 0
        for i in range(k):
            if data[i] == 0:
                res += 1
        ans = res
        for i in range(k, length):
            ans += 1 - data[i]
            ans -= 1 - data[i-k]
            res = min(res, ans)
        return res
