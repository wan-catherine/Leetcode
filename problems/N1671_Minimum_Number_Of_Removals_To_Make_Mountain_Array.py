import bisect
from typing import List


class Solution(object):
    """
    Find LIS(longest increasing sequence) from start and end.
    Then check the largest mountain array.
    """
    def minimumMountainRemovals_(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        prefix, suffix = [0] * length, [0] * length
        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    prefix[i] = max(prefix[i], prefix[j] + 1)
        for i in range(length-2, -1, -1):
            for j in range(length-1, i, -1):
                if nums[j] < nums[i]:
                    suffix[i] = max(suffix[i], suffix[j] + 1)
        s = 3
        for i in range(1, length-1):
            s = max(s, prefix[i] + suffix[i] + 1)

        return length - s

    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_lis(arr):
            stack, res = [], []
            for n in arr:
                index = bisect.bisect_left(stack, n)
                if index == len(stack):
                    stack.append(n)
                else:
                    stack[index] = n
                res.append(index)
            return res

        prefix, suffix = get_lis(nums), get_lis(nums[::-1])
        suffix.reverse()
        s, length = 3, len(nums)
        for i in range(1, length - 1):
            s = max(s, prefix[i] + suffix[i] + 1)

        return length - s

    def minimumMountainRemovals_20241030(self, nums: List[int]) -> int:
        l = len(nums)

        def helper(li):
            if not li:
                return 0
            arr = [li[0]]
            length = 1
            for i, n in enumerate(li[1:]):
                index = bisect.bisect_left(arr, n)
                if index == 0:
                    continue
                if index >= length:
                    length += 1
                    bisect.insort_left(arr, n)
                else:
                    arr[index] = n
            return length

        res = 1
        for i in range(1, l - 1):
            left, right = [-n for n in nums[:i + 1][::-1]], [-n for n in nums[i:]]
            ll, rr = helper(left), helper(right)
            if ll == 1 or rr == 1:
                continue
            res = max(ll + rr - 1, res)

        return l - res
