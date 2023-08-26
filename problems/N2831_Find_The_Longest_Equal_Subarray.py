import collections
from typing import List


class Solution:
    # Loop all index, actually, for specific n here , we only need to loop : nums[i] == n
    def longestEqualSubarray_TLE(self, nums: List[int], k: int) -> int:
        length = len(nums)
        ct = sorted(collections.Counter(nums).most_common(), key=lambda x:-x[1])
        res = 1
        for n, t in ct:
            if res >= t:
                break
            l, r = 0, 0
            while l < length and nums[l] != n:
                l += 1
                r += 1
            original = k
            cur = 0
            while r < length:
                if nums[r] == n:
                    r += 1
                    cur += 1
                elif original > 0:
                    original -= 1
                    r += 1
                else:
                    while l <= r and nums[l] == n:
                        l += 1
                        cur -= 1
                    while l <= r and nums[l] != n:
                        l += 1
                        original += 1
                res = max(res, cur)
        return res

    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        mapping = collections.defaultdict(list)
        for i, n in enumerate(nums):
            mapping[n].append(i)
        res = 1
        for n, li in mapping.items():
            l, r = 0, 1
            original = k
            length = len(li)
            while r < length:
                c = li[r] - li[r-1] - 1
                if c <= original:
                    r += 1
                    original -= c
                else:
                    original += li[l+1] - li[l] - 1
                    l += 1
                res = max(res, r - l)
        return res

