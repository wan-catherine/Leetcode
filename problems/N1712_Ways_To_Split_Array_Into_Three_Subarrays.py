import bisect
from typing import List


class Solution(object):
    def waysToSplit(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(arr)
        prefix = arr[:]
        for i in range(1, length):
            prefix[i] += prefix[i-1]
        total = prefix[-1]
        res = 0
        for i in range(length-2):
            left = prefix[i]
            small = 2* left
            if total - small < left:
                break
            # here if I use : s = bisect.bisect_left(prefix[i+1:], small)
            # it's TLE. Slice actually copy the whole list, so need to avoid it.
            s = bisect.bisect_left(prefix, small)
            if s <= i:
                s = i + 1
            large = (total + left) // 2
            l = bisect.bisect(prefix, large)
            if l <= i:
                l += i + 1
            if l == length or prefix[l] > large:
                l -= 1
            if l == length - 1:
                l -= 1
            if l <= i:
                continue
            res += l - s + 1
        return res % (10**9 + 7)

    def waysToSplit(self, nums: List[int]) -> int:
        length = len(nums)
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        res = 0
        for i in range(1, length):
            left = prefix[i]
            m = 2 * left
            il = bisect.bisect_left(prefix, m)
            il = max(i + 1, il)
            n = (prefix[-1] + left) // 2
            if (prefix[-1] - left) // 2 < left:
                break
            ir = bisect.bisect_right(prefix, n)
            if ir == length + 1:
                ir -= 1
            res += ir - il if ir > il else 0
        return res % (10 ** 9 + 7)
