import bisect
import collections
import sys
from typing import List

"""
similar as 1755
"""

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        ll = length // 2
        def get_sums(li):
            mapping = collections.defaultdict(list)
            sums, length = [(0,0)], len(li)
            for i in range(length):
                temp = [(li[i] + n, c + 1) for n, c in sums]
                i, j, l = 0, 0, len(temp)
                ans = []
                while i < l and j < l:
                    if temp[i][0] < sums[j][0]:
                        ans.append(temp[i])
                        i += 1
                    else:
                        ans.append(sums[j])
                        j += 1
                if i < l:
                    ans.extend(temp[i:])
                else:
                    ans.extend(sums[j:])
                sums = ans
            for n, c in sums:
                mapping[c].append(n)
            return mapping
        lmapping, rmapping = get_sums(nums[:ll]), get_sums(nums[ll:])
        total = sum(nums)
        res = sys.maxsize
        for i in range(1, ll):
            left = lmapping[i]
            right, lr = rmapping[ll-i], len(rmapping[ll-i])
            for n in left:
                v = (total - 2 * n) / 2
                index = bisect.bisect_left(right, v)
                if index >= lr:
                    res = min(res, abs(total - 2 * (right[-1] + n)))
                else:
                    res = min(res, abs(total - 2 * (right[index] + n)))
        res = min(res, abs(lmapping[ll][0] - rmapping[ll][0]))
        return res



