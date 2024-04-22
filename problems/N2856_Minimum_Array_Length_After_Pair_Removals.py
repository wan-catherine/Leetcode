import collections
import heapq
from typing import List

"""Boyer-Moore Algorithm, similar as 229"""


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        ct = collections.Counter(nums)
        length = len(nums)
        count = ct.most_common()[0][1]
        if count > length//2:
            return length - (length - count) * 2
        else:
            return length % 2


