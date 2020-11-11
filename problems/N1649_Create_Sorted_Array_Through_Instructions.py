import bisect
import sys


class Solution(object):
    def createSortedArray_bs(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        res = 0
        nums = [-sys.maxsize, sys.maxsize]
        for i in instructions:
            left, right = bisect.bisect_left(nums, i), bisect.bisect(nums, i)
            res += min(left, len(nums) - right) - 1
            # python has very fast slice operation, so we use it insert or remove , it could be much faster than using insert or pop.
            # bisect.insort_left(nums, i)
            nums[left:left] = [i]
        return res %(10**9 + 7)

    """
    Binary indexed Tree:
    Get parent : index -= index & (-index)
    Get next : index += index & (-index)
    """
    def createSortedArray(self, instructions):
        m = max(instructions)
        arr = [0] * (m + 1)

        # get next
        def update(x):
            while x <= m:
                arr[x] += 1
                x += x & (-x)

        # get parent
        def get(x):
            res = 0
            while x > 0:
                res += arr[x]
                x -= x & (-x)
            return res

        res = 0
        for i, num in enumerate(instructions):
            res += min(get(num-1), i - get(num))
            update(num)
        return res % (10**9+7)